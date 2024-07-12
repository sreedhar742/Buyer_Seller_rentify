from django import forms
from django.contrib.auth.models import User
from .models import Buyers, Sellers

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password', 'email',]

class BuyerForm(forms.ModelForm):
    class Meta:
        model = Buyers
        fields = ['firstname', 'secondname', 'phonenumber',"country"]

class SellerForm(forms.ModelForm):
    class Meta:
        model = Sellers
        fields = ['firstname', 'secondname', 'phonenumber', 'place', 'address']
