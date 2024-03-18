from django.shortcuts import render
from django.db import models
from django.shortcuts import render,redirect
import requests
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
import uuid
from django.core.mail import send_mail
from django.utils import timezone
import urllib3  # Import the timezone module

from api.models import Appointment1, Doctor, Pet
from django.http import HttpResponse
from geopy.geocoders import Nominatim
import folium
from requests.structures import CaseInsensitiveDict
from api.models import Hospital

def home(request):
    return render(request,'homePage.html')
def landing(request):
    return render(request,'landing.html')


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
        hospital = request.POST.get('hospital_names')
        patient_name = request.POST.get('patient_name')
        patient_email = request.POST.get('patient_email')
        health_issue = request.POST.get('healthIssue')
        pet_age = request.POST.get('age')
        appointmentType = request.POST.get('appointmentType')
        appointment_date_time = request.POST.get('appointmentDate')

        # You may want to perform validation here

        # Convert appointment_date_time to a datetime object
        appointment_date = timezone.datetime.strptime(appointment_date_time, "%Y-%m-%d")

        # Create an Appointment instance and save it to the database
        appointment = Appointment1.objects.create(
            hospital=hospital,
            patient_name=patient_name,
            patient_email=patient_email,
            health_issue=health_issue,
            age=pet_age,
            appointmentType=appointmentType,
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


def dlogin(request):
    if request.method == 'POST':
        userid = request.POST['dpetid']
        password = request.POST['dpassword']


        user=auth.authenticate(username=userid,password=password)

        if user is not None:
            # User is authenticated, log them in
            auth.login(request,user)
            return redirect('doctor')
        else:
            error_message = 'Invalid credentials'
            return render(request, 'doctorlogin.html', {'error_message': error_message})

    return render(request, 'doctorlogin.html')


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
        subject = 'Welcome to Medicare'
        message_english = f'Thank you for registering with Medicare. Your Medicare ID is: {petid}. We are excited to have you on board!'
        message_telugu = f'మెడికేర్‌తో నమోదు చేసుకున్నందుకు ధన్యవాదాలు. మీ మెడికేర్ ఐడీ: {petid}. మీరు మాతో చేరడం మాకు ఆనందంగా ఉంది!'
        message_html = f'{message_english}{message_telugu}'        
        from_email = 'lambda428@gmail.com'   # Replace with your email address or a valid email address from which you want to send the email

        # Send the email
        send_mail(subject, message_html, from_email, [email_address])
        #write above like model feilds 


        return render(request, 'login.html')

    return render(request, 'registration.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


def map(request):
    if request.method == 'POST':
        geolocator = Nominatim(user_agent="my_user_agent")
        # Enter the pin code
        pincode = request.POST['pin']  # Example pin code for Buckingham Palace
        alob = Hospital.objects.filter(pincode=pincode).values()
        district = alob[0]['dist']
        print(district)
        disobj = Hospital.objects.filter(dist=district).values()
        print(disobj)
        #loc = geolocator.geocode(pincode)
        mymap=folium.Map(location=[0,0],zoom_start=9)
        for i in disobj:
            try:
                latt,logg = coord(urllib3.parse.quote(i['Address']))
                if(latt is None or logg is None):
                    continue
            except:
                continue
            folium.Marker([latt,logg],popup="myloc",tooltip=i['hname']).add_to(mymap)
            folium_map_html = mymap._repr_html_()
        return render(request,"bookAppointment.html",{"folium_map_html": folium_map_html, "disobj": disobj})
    return render(request, "bookAppointment.html")


import requests
from requests.structures import CaseInsensitiveDict

def coord(address):
    url = "https://api.geoapify.com/v1/geocode/search?text="+str(address)+"&apiKey=a1b07ce765f14402b307e1edb02f6920"
    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        data = resp.json()
        if 'features' in data and data['features']:
            result = data['features'][0]
            latitude = result['properties']['lat']
            longitude = result['properties']['lon']
            return latitude,longitude
    return None



def doctor(request):
    appointments=Appointment1.objects.all()
    print(appointments)
    
    return render(request,'doctor.html',{'appointments':appointments})


def dregistration(request):
    if request.method == 'POST':
        first_name = request.POST['dpetname']
        specialization = request.POST['downermail']
        password = request.POST['password']
        hospital = request.POST['dpetage']
        user=User.objects.create_user(username=first_name, password=password)
        user.save()
        doctor = Doctor.objects.create(
            first_name=first_name,
            specialization=specialization,
            password=password,
            hospital=hospital
            
        )
        

        return redirect('dlogin')

    return render(request, 'dregistration.html')