from django.shortcuts import render, redirect, get_object_or_404
from django.http import Http404
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *

def profile_view(request, username=None):
    if username:
        profile = get_object_or_404(User, username=username).profile
    else:
        try:
            profile = request.user.profile
        except:
            raise Http404()
        
    context = {
        'profile' : profile
    }
    
    return render(request, 'profile.html', context)
@login_required
def profile_edit(request):
    form = ProfileForm(instance=request.user.profile)
    
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    if request.path == reverse('profile-onboarding'):
        template = 'profile_onboarding.html'
    else:
        template = 'profile_edit.html'
        
    
    context = {
        'form' : form,
        'template' : template
    }
    
    return render(request, 'profile_edit.html', context)

@login_required
def profile_delete(request):
    user = request.user
    
    if request.method == 'POST':
        logout(request)
        user.delete()
        messages.success(request, 'Account deleted, what a pity')
        
        return redirect('home')
        
    return render( request, 'profile_delete.html')
    
