from django.db import models

DESCRIPTIONS = (
    (0,"Sunny"),
    (1,"Rain"),
    (2,"Cloudy"),
    (3,"Snow"),
    (4,"Shady"),
    (5,"Windy"),
    (6,"foggy"),
    (7,"hot"),
    (8,"chill"),
    
)
COUNTRYS = (
    (0,"India"),
    (1,"USA"),
    (2,"China"),
    (3,"Algeria"),
    (4,"Denmark"),
    (5,"France"),
    
)


# Created  models here to discride weather
class Description(models.Model):
    place =               models.CharField( max_length=100)
    weather_discription = models.IntegerField(choices=DESCRIPTIONS,default=0)
    coordinate =          models.FloatField()
    temp =                models.FloatField(("Temprature"))
    humidity =            models.IntegerField()
    windspeed =           models.IntegerField()
    country =             models.IntegerField(choices=COUNTRYS,default=0)
    date =                models.DateTimeField( auto_now=True, auto_now_add=False)
 
 
    def __str__(self):
       return self.place
  
 