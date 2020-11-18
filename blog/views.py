import csv 
from django.shortcuts import render
from django.http import HttpResponse
from .models import Airport




def home(request):

    airport =Airport.objects.all()
    context = {'airport':airport}
    return render(request,'blog/home.html',context)
    
    

def about(request):
    return render(request,'blog/about.html')

        
    