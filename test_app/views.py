from django.shortcuts import render, redirect
from .models import *
from django.forms import ModelForm
from django import forms
from bs4 import BeautifulSoup
import requests

# Home Page Method
def home(request):
    # Get all Posts from the Database
    posts = Post.objects.all()
    
    context = {
        'posts' : posts
    }
    
    return render(request, "posts/home.html", context)

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

# Create Post Method
def post_create_view(request):
    # Grab the form for the View
    form = PostCreateForm()
    
    # Check if the form has been submitted
    if request.method == 'POST':
        # Get the information submitted by the user
        form = PostCreateForm(request.POST)
        # Validate the form
        if form.is_valid():
            # Create a variable that tells the form not to save yet
            post = form.save(commit=False)
            # Create a variable that gets the url that the user entered in the form from the website
            website = requests.get(form.data['url'])
            # A variable that tells BeautifulSoup to turn the Website variable into text and parse it with the html.parser
            sourcecode = BeautifulSoup(website.text, 'html.parser')

            # Find the url that starts with this meta content and ends with the sourcecode variable
            find_image = sourcecode.select('meta[content^="https://live.staticflickr.com/"]')
            # Select only the first item that returns from the find_image variable
            image = find_image[0]['content']
            # Attach that image to the post variable
            post.image = image

            # Find the title of the title 
            find_title = sourcecode.select('h1.photo-title')
            # Select only the first item that returns from the find_title variable convert it to text and eliminate the whitespace
            title = find_title[0].text.strip()
            # Attach the title to the post variable
            post.title = title

            # Find the artist
            find_artist = sourcecode.select('a.owner-name')
            # Select only the first item that returns from the find_artist variable convert it to text and eliminate the whitespace 
            artist = find_artist[0].text.strip()
            # Attach the artist to the post variable
            post.artist = artist

            # Save the form
            post.save()
            # Send the user back to the home page
            return redirect('home')
            
    context = {
        'form' : form
    }
    
    return render(request, 'posts./post_create.html', context)