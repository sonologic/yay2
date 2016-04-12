from django.forms import ModelForm, CharField, PasswordInput
from studio.models import SourceAlsa, SinkIcecast


class SourceAlsaForm(ModelForm):
    class Meta:
        model = SourceAlsa
        fields = [  'name',
                    'strip_blank',
                    'alsa_device'
                 ]

class SinkIcecastForm(ModelForm):
    #password = CharField(widget=PasswordInput())

    class Meta:
        model = SinkIcecast
        fields = [  'name',
                    'server',
                    'port',
                    'mount',
                    'username',
                    'password',
                    'source'
                 ]
