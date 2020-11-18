from django.db import models

class Airport(models.Model):
    iata = models.CharField(max_length = 4)
    icao = models.CharField(max_length = 4)
    airport_name = models.TextField()
    location = models.TextField()
    gps = models.TextField()
    
def __str__(self):
    return self.iata


