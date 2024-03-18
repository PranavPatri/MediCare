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
    
class Appointment1(models.Model):
    hospital = models.CharField(max_length=255,default="hospital")
    patient_name = models.CharField(max_length=255)
    patient_email = models.EmailField(default="test@gmail.com")
    health_issue = models.CharField(max_length=1000)
    age=models.IntegerField(default=0)
    appointmentType=models.CharField(max_length=255)
    appointment_date_time = models.DateField()

    def __str__(self):
        return str(self.patient_name)


class Hospital(models.Model):
    hid=models.CharField(max_length=50)
    hnumber=models.CharField(max_length=20,default="-")
    hmail=models.CharField(max_length=500,default="hospital@gmail.com")
    hname=models.CharField(max_length=500)
    pincode=models.CharField(max_length=6)
    state=models.CharField(max_length=50)
    dist=models.CharField(max_length=60)
    Address=models.CharField(max_length=100)
    speciality=models.CharField(max_length=100)
   
   
class Doctor(models.Model):
    first_name = models.CharField(max_length=100, primary_key=True) 
    specialization = models.CharField(max_length=150)
    password = models.CharField(max_length=150)
    hospital = models.CharField(max_length=150)
    # Add any other fields relevant to the doctor

    def _str_(self):
        return self.first_name