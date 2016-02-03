from django.contrib import admin

# Register your models here.
from .models import Build, Application

admin.site.register(Build)
admin.site.register(Application)