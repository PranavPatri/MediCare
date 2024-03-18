
from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("api.urls")),
    path('', views.landing,name="landing"),
    path('home/', views.home,name="home"),
    path('disease_prediction/', views.diseasePrediction,name="diseasePrediction"),
    path('chat/', views.chatBot,name="chat"),
    path('authentication/', views.userAuthentication,name="authentication"),
    path('book_appointment/', views.bookAppointment, name='bookAppointment'),
    path('book_appointment/', views.bookAppointment, name='bookAppointment'),
    path('appointment_form1/', views.appointment_form,name="appointment_form"),
    path('products/', views.products,name="products"),
    path('donate/', views.donate,name="donate"),
    path('login/', views.login,name="login"),
    path('register/', views.registration,name="registration"),
    path('logout/', views.logout,name="logout"),    

    path('nearby/', views.map, name='nearby'),
    path('doctor/', views.doctor, name='doctor'),
    path('dregistration/', views.dregistration, name='dregistration'),
    path('dlogin/', views.dlogin, name='dlogin'),
    
]
