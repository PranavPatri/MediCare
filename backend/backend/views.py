from django.shortcuts import render
from django.db import models
from django.shortcuts import render,redirect
import requests
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
import uuid
from django.core.mail import send_mail
from django.utils import timezone  # Import the timezone module

from api.models import Pet, Appointment
from django.http import HttpResponse

def home(request):
    return render(request,'homePage.html')


def diseasePrediction(request):
    return render(request,'diseasePrediction.html')


def chatBot(request):
    return render(request,'chatBotPage.html')


def userAuthentication(request):
    return render(request,'authenticationPage.html')


def bookAppointment(request):
    return render(request,'bookAppointment.html')


def appointment_form(request):
    if request.method == 'POST':
        hospital = request.POST.get('hospital')
        pet_name = request.POST.get('petName')
        owner_name = request.POST.get('ownerName')
        health_issue = request.POST.get('healthIssue')
        pet_gender = request.POST.get('petGender')
        appointment_date_time = request.POST.get('appointmentDateTime')

        # You may want to perform validation here

        # Convert appointment_date_time to a datetime object
        appointment_date_time = timezone.datetime.strptime(appointment_date_time, "%Y-%m-%dT%H:%M")

        # Create an Appointment instance and save it to the database
        appointment = Appointment.objects.create(
            hospital=hospital,
            pet_name=pet_name,
            owner_name=owner_name,
            health_issue=health_issue,
            pet_gender=pet_gender,
            appointment_date_time=appointment_date_time
        )

        # You can add additional logic here, e.g., sending confirmation emails

        return redirect('home')  # Redirect to a success page or home page

    return HttpResponse('<h1>Invalid request</h1>')  # Return an error message if the request method is not POST


def products(request):
    return render(request,'products.html')


def donate(request):
    return render(request,'donatePage.html')


def login(request):
    if request.method == 'POST':
        userid = request.POST['petid']
        password = request.POST['password']


        user=auth.authenticate(username=userid,password=password)

        if user is not None:
            # User is authenticated, log them in
            auth.login(request,user)
            return redirect('home')
        else:
            error_message = 'Invalid credentials'
            return render(request, 'login.html', {'error_message': error_message})

    return render(request, 'login.html')


def registration(request):
    if request.method == 'POST':
        petname = request.POST['petname']  # Assuming 'userid' is the email
        ownermail= request.POST['ownermail']  # Assuming 'userid' is the email
        petage = request.POST['petage']  # Assuming 'userid' is the email
        petgender = request.POST['gender']  # Assuming 'userid' is the email
        password = request.POST['password']  # Assuming 'password' is the registration number

        petid = str(uuid.uuid4())
        
        user=User.objects.create_user(username=petid, password=password)
        user.save()
        pets = Pet.objects.create(
            petid=petid,
            ownermail=ownermail,
            petname=petname,
            petgender=petgender,
            petage=petage,
            password=password
            
        )
        email_address = pets.ownermail

        # Compose the email message
        subject = 'Welcome to PetCare'
        message = f'Thank you for registering with PetCare. Your Pet ID is: {petid}. We are excited to have you on board!'
        from_email = 'lambda428@gmail.com'   # Replace with your email address or a valid email address from which you want to send the email

        # Send the email
        send_mail(subject, message, from_email, [email_address])
        #write above like model feilds 


        return render(request, 'login.html')

    return render(request, 'registration.html')


def logout(request):
    auth.logout(request)
    return redirect('home')