from django.forms import ModelForm
from django import forms
from .models import *

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
        label = {
            'realname' : 'Name',
        }
        widgets = {
            'image' : forms.FileInput(),
            'bio' : forms.Textarea(attrs={'rows': 3})
        }