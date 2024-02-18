from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone

class Pet(models.Model):
    petid = models.CharField(max_length=100, blank=True, primary_key=True)
    ownermail=models.EmailField()
    petname = models.CharField(max_length=100)
    petgender = models.CharField(max_length=100)
    petage = models.IntegerField()
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return str(self.petid)
    
class Appointment(models.Model):
    hospital = models.CharField(max_length=255)
    pet_name = models.CharField(max_length=255)
    owner_name = models.CharField(max_length=255)
    health_issue = models.CharField(max_length=255)
    pet_gender = models.CharField(max_length=6)
    appointment_date_time = models.DateTimeField()

    def __str__(self):
        return str(self.pet_name)

