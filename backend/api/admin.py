from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Pet, Appointment


admin.site.register(Pet)
admin.site.register(Appointment)
