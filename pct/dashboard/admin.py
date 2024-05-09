from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(theatre_manager)
admin.site.register(theatre)
admin.site.register(screen)
admin.site.register(movie)
admin.site.register(show)
admin.site.register(User1)
