from django.contrib import admin
from .models import *

# Make models availible in the adim site
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(LikedPost)

