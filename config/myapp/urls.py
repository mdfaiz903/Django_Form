from django.urls import path
from . views import show,successfull
urlpatterns = [
    path ('',show),
    path ('successfull/',successfull,name='successfull'),
]
