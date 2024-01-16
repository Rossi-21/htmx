from django.dispatch import receiver
from django.shortcuts import get_object_or_404
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from .models import Profile

# Create a profile when a user is create
@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    user = instance
    # If a user instace is created
    if created:
        # Create a Profile object for that user where the user and email are the same
        Profile.objects.create(
            user = user,
            email = user.email
        )
    # If a user is not created then it is being updated
    else:
        profile = get_object_or_404(Profile, user=user)
        profile.email = user.email
        profile.save()

# Update the user info at the same time the profile is updated
@receiver(post_save, sender=Profile)
def update_user(sender, instance, created, **kwargs):
    profile = instance
    # If the action is not profile creation ie.. the profile is updated
    if created == False:
        # Get the user object associated with the profile
        user = get_object_or_404(User, id=profile.user.id)
        # If the user email and profile email are not the same make the the same
        if user.email != profile.email:
            user.email = profile.email
            user.save()
        
