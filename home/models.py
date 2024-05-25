from django.db import models
from django.contrib.auth.models import User

class Buyers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    secondname = models.CharField(max_length=100)
    email = models.EmailField()  # corrected from 'eemail'
    phonenumber = models.CharField(max_length=15)  # changed to CharField
    
    def __str__(self) -> str:
        return f"{self.user}"
    

class Sellers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    secondname = models.CharField(max_length=100)
    email = models.EmailField()  # corrected from 'eemail'
    phonenumber = models.CharField(max_length=15)  # changed to CharField
    place = models.CharField(max_length=100)
    address = models.TextField()  # max_length is not required for TextField
    
        
    def __str__(self):
        return f"{self.user}"
    