from django.db import models
from django.contrib.auth.models import User

class Buyers(models.Model):
    COUNTRY_CHOICES = [
        ('india', 'India'),
        ('pakistan', 'Pakistan'),
        ('bangladesh', 'Bangladesh'),
        ('srilanka', 'Sri Lanka'),
        ('china', 'China'),
        ('bhutan', 'Bhutan'),
    ]
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    secondname = models.CharField(max_length=100)
    email = models.EmailField()  
    phonenumber = models.CharField(max_length=15)  
    country = models.CharField(choices=COUNTRY_CHOICES, max_length=100)
    
    def __str__(self) -> str:
        return f"{self.user}"

    

class Sellers(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100)
    secondname = models.CharField(max_length=100)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=15)  
    place = models.CharField(max_length=100)
    address = models.TextField() 
        
    def __str__(self):
        return f"{self.user}"
    
    
    