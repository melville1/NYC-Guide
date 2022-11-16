from django.shortcuts import render

from django.http import HttpResponse
from django.views import View

# Create your views here.

class Homepage(View):
    def get(self, request):
        return HttpResponse('Welcome to NYC Guide')