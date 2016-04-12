import pytz
from datetime import datetime
from time import sleep

import signal
from django.core.management.base import BaseCommand, CommandError
from studio.models import Configuration, Logfile, LogfileEntry, BackgroundProcess
import os
from multiprocessing import Process
import subprocess

from yay2web.utils import generate_liquidsoap_config

from yay2web.utils import string_to_filename




class Command(BaseCommand):
    help = 'Start the liquidsoap process manager'

    #def add_arguments(self, parser):
    #    parser.add_argument('poll_id', nargs='+', type=int)

    def child(self):
        self.stdout.write("Starting liquidsoap")

        sub = subprocess.call(["liquidsoap",os.path.join(self.config.cmd_path, "yay2.liq")])

        return sub

    def get_or_create_log(self):
        logs = Logfile.objects.filter(name__exact='liquidsoap')

        if len(logs)==0:
            log = Logfile(name='liquidsoap')
            log.save()
            return log

        if len(logs)==1:
            return logs[0]

        raise CommandError("More than one log with name 'liquidsoap' found, configuration is corrupt")

    def get_or_create_bg_process(self):
        processes = BackgroundProcess.objects.filter(name__exact='liquidsoap')

        if len(processes) == 0:
            process = BackgroundProcess(name='liquidsoap')
            return process

        if len(processes) == 1:
            return processes[0]

        raise CommandError("More than one background process with name 'liquidsoap' found, configuration is corrupt")

    def handle_signal(self, signal, frame):
        self.interrupted = True

    def handle(self, *args, **options):
        self.config = Configuration.objects.get()

        self.ls_config = generate_liquidsoap_config()

        self.log_path = os.path.join(self.config.log_path, string_to_filename(self.config.station_name)+".log")

        config_file = file(os.path.join(self.config.cmd_path, "yay2.liq"), "w+")
        config_file.write(self.ls_config)
        config_file.close()

        log = self.get_or_create_log()

        bg_process = self.get_or_create_bg_process()
        bg_process.logfile = log

        # todo: verify that bg_process.pid is not already running

        self.interrupted = False
        signal.signal(signal.SIGINT, self.handle_signal)

        p = Process(target=self.child)

        log_file = file(self.log_path)

        log_file.seek(0,2)

        prev_pos = log_file.tell()

        p.start()

        bg_process.started_at = datetime.now(pytz.UTC)
        bg_process.pid = p.pid
        bg_process.save()

        while (not self.interrupted) and p.is_alive():
            log_file.seek(0,2)
            pos = log_file.tell()
            if not pos==prev_pos:
                log_file.seek(prev_pos)

                line = log_file.readline().strip()

                entry = LogfileEntry(logfile=log, message=line)
                entry.save()

                prev_pos = log_file.tell()
            else:
                sleep(0.1)

        if not p.is_alive():
            self.stdout.write("process died")

        if self.interrupted:
            self.stdout.write("ctrl-c pressed, aborting")
            p.terminate()

        p.join()

        bg_process.delete()

        #for poll_id in options['poll_id']:
        #    try:
        #        poll = Poll.objects.get(pk=poll_id)
        #    except Poll.DoesNotExist:
        #        raise CommandError('Poll "%s" does not exist' % poll_id)
        #
        #            poll.opened = False
        #            poll.save()
        #
        #            self.stdout.write(self.style.SUCCESS('Successfully closed poll "%s"' % poll_id))
