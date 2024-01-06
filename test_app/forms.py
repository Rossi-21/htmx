from django.forms import ModelForm
from django import forms
from .models import *

class PostCreateForm(ModelForm):
    class Meta:
        # Select the model used in the form
        model = Post
        # Select the fields you wish to display
        fields = ['url', 'body', 'tags']
        # Change the label if desired
        labels = {
            'body' : 'Caption',
            'tags' : 'Category',
        }
        # Add attributes to the form through widget functionality
        widgets = {
            'body' : forms.Textarea(attrs={'rows': 3, 'placeholder': 'Add a caption...', 'class': 'font1 text-4xl'}),
            'url' : forms.TextInput(attrs={'placeholder': 'Add url...'}),
            'tags' : forms.CheckboxSelectMultiple(),
        }
        
class PostEditForm(ModelForm):
    class Meta:
        model = Post
        fields = ['body', 'tags']
        labels = {
            'body' : '',
            'tags' : 'Category',
        }
        widgets = {
            'body' : forms.Textarea(attrs={'rows': 3, 'class': 'font1 text-4xl'}),
            'tags' : forms.CheckboxSelectMultiple(),
        }