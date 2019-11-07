from django.db import models
from django.contrib.auth.models import User

class user(User):
    itinerary=models.CharField(max_length=500)
    is_leader=models.BooleanField(default=False)
    phone_number=models.CharField(max_length=13)

class Leader(models.Model):
    userID=models.OneToOneField(user,on_delete=models.CASCADE)
    nationalID=models.CharField(max_length=12)
    has_car=models.BooleanField(default=False)
    car_capacity=models.CharField(max_length=5)
    car_model=models.CharField(max_length=20)