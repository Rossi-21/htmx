from django.forms import ModelForm
from django import forms
from .models import *

class PostCreateForm(ModelForm):
    class Meta:
        # Select the model used in the form
        model = Post
        # Select the fields you wish to display
        fields = ['url', 'body']
        # Change the label if desired
        labels = {
            'body' : 'Caption'
        }
        # Add attributes to the form through widget functionality
        widgets = {
            'body' : forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a caption...', 'class': 'font1 text-4xl'}),
            'url' : forms.TextInput(attrs={'placeholder': 'Add url...'}),
        }
        
class PostEditForm(ModelForm):
    class Meta:
        model = Post
        fields = ['body']
        labels = {
            'body' : '',
        }
        widgets = {
            'body' : forms.Textarea(attrs={'rows': 3, 'class': 'font1 text-4xl'})
        }