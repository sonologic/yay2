import psutil
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

    def get_or_create_log(self, name):
        logs = Logfile.objects.filter(name__exact=name)

        if len(logs)==0:
            log = Logfile(name=name)
            log.save()
            return log

        if len(logs)==1:
            return logs[0]

        raise CommandError("More than one log with name '{0}' found, configuration is corrupt")

    def get_or_create_bg_process(self):
        processes = BackgroundProcess.objects.filter(name__exact='liquidsoap')

        if len(processes) == 0:
            process = BackgroundProcess(name='liquidsoap')
            return process

        if len(processes) == 1:
            return processes[0]

        raise CommandError("More than one background process with name 'liquidsoap' found, configuration is corrupt")

    def log_message(self, msg, abort=False):
        self.stdout.write(msg)
        entry = LogfileEntry(logfile=self.log, message=msg)
        entry.save()
        if abort:
            raise CommandError(msg)

    def write_ls_config(self):
        # generate liquidsoap configuration
        ls_config = generate_liquidsoap_config()
        config_file = file(os.path.join(self.config.cmd_path, "yay2.liq"), "w+")
        config_file.write(ls_config)
        config_file.close()

    def already_running_on_pid(self, pid):
        if not psutil.pid_exists(pid):
            return False

        p = psutil.Process(pid)
        if p.name=='liquidsoap':
            return True

        return False

    def wait_for_file(self, filename, timeout=10, delay=0.2):
        retry = int(timeout / delay)
        while not os.path.isfile(filename) and retry > 0:
            sleep(delay)
            retry -= 1

        return os.path.isfile(filename)

    def log_file_reader_init(self, timeout=10, delay=0.2):
        if not self.wait_for_file(self.log_path):
            return False

        self.log_file = file(self.log_path)

        self.log_file.seek(0, 2)

        self.log_file_prev_pos = self.log_file.tell()

        return True

    def log_file_reader_readline(self):
        self.log_file.seek(0, 2)
        pos = self.log_file.tell()

        if not pos == self.log_file_prev_pos:
            self.log_file.seek(self.log_file_prev_pos)
            line = self.log_file.readline().strip()
            self.log_file_prev_pos = self.log_file.tell()
            return line

        return None

    def is_running(self,bg_process):
        self.log_message("old pid is {0}".format(bg_process.pid))

        if bg_process.pid != None:
            if self.already_running_on_pid(bg_process.pid):
                return False
            else:
                bg_process.pid = None
                bg_process.running = False
                bg_process.terminate = False
                bg_process.save()

        if os.path.isfile(self.pidfile_path):
            pid = int(file(self.pidfile_path).read().strip())
            if self.already_running_on_pid(pid):
                return True
            os.unlink(self.pidfile_path)

        return False

    def start_liquidsoap(self, bg_process):
        self.log_message("Starting liquidsoap process")

        if os.path.isfile(self.log_path):
            os.unlink(self.log_path)

        bg_process.started_at = datetime.now(pytz.UTC)
        bg_process.running = True
        bg_process.save()

        subprocess.call(["liquidsoap", os.path.join(self.config.cmd_path, "yay2.liq")])

        # wait for pid file
        if not self.wait_for_file(self.pidfile_path):
            bg_process.running = False
            bg_process.save()
            self.log_message("timeout waiting for pid file, aborting", True)

        pid = int(file(self.pidfile_path).read().strip())
        self.log_message("PID is {0}".format(pid))

        bg_process.pid = pid
        bg_process.save()

        return pid

    def update_process_stopped(self, bg_process):
        bg_process.stopped_at = datetime.now(pytz.UTC)
        bg_process.pid = None
        bg_process.running = False
        bg_process.terminate = False
        bg_process.save()

    def handle_signal(self, signal, frame):
        self.interrupted = True

    def handle(self, *args, **options):
        self.log = self.get_or_create_log('process_manager')

        self.log_message("Process manager starting")

        # load yay2 configuration
        self.config = Configuration.objects.get()
        self.pidfile_path = os.path.join(self.config.cmd_path, string_to_filename(self.config.station_name)) + '.pid'
        self.log_path = os.path.join(self.config.log_path, string_to_filename(self.config.station_name) + ".log")


        ls_log = self.get_or_create_log('liquidsoap')

        bg_process = self.get_or_create_bg_process()
        bg_process.logfile = ls_log
        bg_process.terminate = False
        bg_process.running = False
        bg_process.start = False
        bg_process.save()

        if self.is_running(bg_process):
            self.log_message("liquidsoap already running", True)

        # generate liquidsoap configuration
        self.write_ls_config()

        #
        # mainloop
        #
        pid = None
        self.interrupted = False
        signal.signal(signal.SIGINT, self.handle_signal)
        while not self.interrupted:
            bg_process = BackgroundProcess.objects.get(name='liquidsoap')
            idle = True
            if bg_process.running:
                if pid!=None and not self.already_running_on_pid(pid):
                    # process died, update db
                    self.update_process_stopped(bg_process)
                    self.log_message("liquidsoap process died")

            if self.already_running_on_pid(pid):
                line = self.log_file_reader_readline()
                if line!=None:
                    entry = LogfileEntry(logfile=ls_log, message=line)
                    entry.save()
                    idle = False

            if (not bg_process.running) and (not self.already_running_on_pid(pid)) and bg_process.start:
                pid = self.start_liquidsoap(bg_process)

                if not self.log_file_reader_init():
                    pid = None
                    os.kill(pid, 9)
                    self.update_process_stopped(bg_process)
                    self.log_message("timeout waiting for log file, killed process (if not already dead)")
                else:
                    bg_process.start = False
                    bg_process.running = True
                    bg_process.terminate = False
                    bg_process.save()

            if bg_process.running and bg_process.terminate:
                os.kill(pid, 9)
                pid = None
                self.update_process_stopped(bg_process)
                self.log_message("terminated liquidsoap on user request")

            if idle:
                sleep(0.1)

            #self.log_message("bg_process terminate is {0}, running is {1}, start is {2}".format(bg_process.terminate, bg_process.running, bg_process.start))

        if pid!=None and not self.already_running_on_pid(pid):
            self.log_message("process died")

        if self.interrupted:
            self.log_message("SIGINT received, aborting")
            os.kill(pid, 9)

        # flush log
        line = self.log_file_reader_readline()
        while line!=None:
            entry = LogfileEntry(logfile=ls_log, message=line)
            entry.save()
            line = self.log_file_reader_readline()

        # update database
        self.update_process_stopped(bg_process)

        self.log_message("Process manager exiting")