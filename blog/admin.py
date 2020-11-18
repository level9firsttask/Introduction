from django.contrib import admin

from .models import Airport

@admin.register(Airport)
class PetAdmin(admin.ModelAdmin):   
    list_display = ['iata','icao','airport_name','location','gps']


