
# imports are made to connect the borough dictionary and the View class coming from django

from django.shortcuts import render


from django.views import View
from nycAPP.boroughs import boroughs
# Create your views here.




# this is the homepage where all the boroughs will be displayed. 
# the context variable is sent to the city.html template
class CityView(View):
    def get(self, request,):
        
        return render(request=request, 
                        template_name='city.html',
                         context={'boroughs': boroughs.keys()})


# this borough view will display the activities of each borough
# this view takes in borough argument 
#the context vairiable will be passed to the borough.html template
class BoroughView(View):
    def get(self, request, borough):
        return render(
            request=request,
            template_name='borough.html',
            context={'borough': borough, 'activities': boroughs[borough].keys()},
        )

# this activity view will display all venues
# this view takes in the borough and activity required
class ActivityView(View):
    def get(self, request, borough, activity):
        return render(
            request = request,
            template_name='activity.html',
            context = {'borough': borough, 
                       'activity': activity, 
                       'venues': boroughs[borough][activity].keys() }
        )

# this view displayes the image and description of a particular venue.
class VenueView(View):
    def get(self,request, borough, activity, venue):
        return render(
            request = request,
            template_name = 'venue.html',
            context = {'venue':venue, 
                       'img_link': boroughs[borough][activity][venue]['img_link'],
                       'description': boroughs[borough][activity][venue]['description'],
                       }
        )

       