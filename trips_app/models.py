from django.db import models
from django.contrib.auth.models import User

class Locations(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    latitude = models.FloatField()
    longitude = models.FloatField()
    location = models.CharField(max_length=300)
    speed = models.CharField(max_length=100)
    altitude = models.CharField(max_length=100)
    date_time = models.DateTimeField(max_length=120)


    def __str__(self):
        return self.location



class Trips(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task = models.CharField(max_length=100)
    done = models.BooleanField(default=False)

    def __str__(self):
        return self.task + "-" + str(self.done)



