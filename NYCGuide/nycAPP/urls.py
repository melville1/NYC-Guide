from django.urls import path 
from nycAPP.views import CityView,BoroughView, ActivityView, VenueView 

# This is the where we create the path urls for each view. 

urlpatterns = [
    # the empty string will take us to the home page. 
    path('', CityView.as_view(), name='city'),
    # once the boroughs is clickied, it will take us to the borough view.
    path('<str:borough>', BoroughView.as_view(), name='borough'),
    # the same happens to the following lines of code.
    path('<str:borough>/<str:activity>', ActivityView.as_view(), name='activity'),
    path('<str:borough>/<str:activity>/<str:venue>', VenueView.as_view(), name='venue')
    
]