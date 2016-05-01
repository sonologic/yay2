from django.forms import ModelForm, CharField, PasswordInput, Form
from studio.models import SourceAlsa, SinkIcecast

class LoginForm(Form):
    username = CharField(max_length=30)
    password = CharField(max_length=128, widget=PasswordInput())

    def clean(self):
        cleaned_data = super(LoginForm, self).clean()

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
