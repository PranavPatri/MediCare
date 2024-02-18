
from django.urls import path
from . import views
urlpatterns = [
    path('predict/',views.predict_disease),
    path('getresponse/',views.get_response_bot),
]