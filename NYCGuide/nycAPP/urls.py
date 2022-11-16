from django.urls import path 
from nycAPP.views import Homepage


urlpatterns = [
path('', Homepage.as_view(), )







]