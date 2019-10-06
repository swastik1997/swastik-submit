from django.contrib import admin

from .models import User,Album,Photo

admin.site.register(User)
admin.site.register(Album)
admin.site.register(Photo)