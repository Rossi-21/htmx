from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from bs4 import BeautifulSoup
import requests
from django.contrib import messages
from .forms import *

# Home Page Method
def home(request):
    # Get all Posts from the Database
    posts = Post.objects.all()
    
    context = {
        'posts' : posts
    }
    
    return render(request, "posts/home.html", context)

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
    
    # Display the Post Creation Page
    return render(request, 'posts./post_create.html', context)

# Delete Post Method
def post_delete_view(request, pk):
    # Get the Post from the Database or display a 404 page
    post = get_object_or_404(Post, id=pk)
    # If the User sends the form
    if request.method == 'POST':
        # Delete the post
        post.delete()
        # Display a success message to the User
        messages.success(request, 'Post deleted')
        # Send the User back to the home page
        return redirect('home')
        
    context = {
        'post': post
    }
    return render(request, 'posts/post_delete.html', context)

# Edit Post Method
def post_edit_view(request, pk):
    # Get the Post from the Database or display a 404 page
    post = get_object_or_404(Post, id=pk)
    # Get the Form 
    form = PostEditForm(instance=post)
    # If the User send the form 
    if request.method == 'POST':
        # Use the Post Edit Form
        form = PostEditForm(request.POST, instance=post)
        # Validate the form
        if form.is_valid():
            # Save the form to the Database
            form.save()
            # Dispay a success message to the User
            messages.success(request, 'Post updated')
            # Send the User back to the home page
            return redirect('home')
            
    context = {
        'post' : post,
        'form' : form
    }
    
    return render(request, 'posts/post_edit.html', context)

# Display Post Method
def post_page_view(request, pk):
    # Get the post from the Database or display a 404 page
    post = get_object_or_404(Post, id=pk)
    
    context = {
        'post' : post
    }
    return render(request, 'posts/post_page.html', context)

