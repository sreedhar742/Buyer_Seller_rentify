# urls.py
from django.urls import path
from .views import register_buyer, register_seller, custom_login, custom_logout, profile

urlpatterns = [
    path('register/buyer/', register_buyer, name='register_buyer'),
    path('register/seller/', register_seller, name='register_seller'),
    path('login/', custom_login, name='login'),
    path('logout/', custom_logout, name='logout'),
    path('profile/', profile, name='profile'),
]
