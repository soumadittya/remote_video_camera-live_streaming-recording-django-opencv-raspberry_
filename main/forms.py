from .models import Settings
from django import forms

class Settings_Form(forms.ModelForm):
    class Meta:
        model = Settings
        fields = ['path', 'recording', 'fps']
        if Settings.objects.get(pk = 1).recording == True:
            widgets = {
            'path' : forms.TextInput(
                attrs = {'value' : Settings.objects.get(pk =1).path}),
            'recording' : forms.CheckboxInput(
                attrs = {'checked' : "on"}),
            'fps' : forms.TextInput(
                attrs = {'Value' : Settings.objects.get(pk = 1).fps,
                         'class' : 'vIntegerField',
                         'type' : 'number',
                         'min' : "5",
                         'max' : "30"})
            }
        else:
            widgets = {
                'path': forms.TextInput(
                    attrs={'value': Settings.objects.get(pk=1).path}),
                'fps': forms.TextInput(
                    attrs={'Value': Settings.objects.get(pk=1).fps,
                           'class': 'vIntegerField',
                           'type': 'number',
                           'min': "5",
                           'max': "30"})
            }

        # def recording_status(self):
        #     if Settings.objects.get(pk=1).recording == True:
        #         return "yes"
        #     else:
        #         return "false"
