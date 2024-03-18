from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Pet, Appointment1, Hospital, Doctor


admin.site.register(Pet)
admin.site.register(Appointment1)
admin.site.register(Hospital)
admin.site.register(Doctor)
