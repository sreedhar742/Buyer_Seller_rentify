from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm, BuyerForm, SellerForm

from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.conf import settings
from django.core.mail import send_mail
from .forms import UserForm, BuyerForm

def register_buyer(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        buyer_form = BuyerForm(request.POST)
        if user_form.is_valid() and buyer_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            buyer = buyer_form.save(commit=False)
            buyer.user = user
            buyer.save()
            login(request, user)
            subject = 'Welcome to Rentify!'
            message = f'Hi {user.username}, thank you for registering on Rentify.'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [user.email,]
            try:
                send_mail(subject, message, email_from, recipient_list)
            except Exception as e:
                # Optional: Add logging or user notification of email failure
                print(f"Error sending email: {e}")
            return redirect('login')
    else:
        user_form = UserForm()
        buyer_form = BuyerForm()
    return render(request, 'register_buyer.html', {'user_form': user_form, 'buyer_form': buyer_form})


def register_seller(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        seller_form = SellerForm(request.POST)
        if user_form.is_valid() and seller_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            seller = seller_form.save(commit=False)
            seller.user = user
            seller.save()
            login(request, user)
            return redirect('login')
    else:
        user_form = UserForm()
        seller_form = SellerForm()
    return render(request, 'register_seller.html', {'user_form': user_form, 'seller_form': seller_form})


# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm

def custom_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('profile')  # Redirect to a success page.
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def custom_logout(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout.


# views.py
# views.py
# views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Buyers, Sellers

@login_required
def profile(request):
    user = request.user
    try:
        buyer = Buyers.objects.get(user=user)
        profile_type = 'buyer'
        seller_details = Sellers.objects.all()  # If the user is a buyer, show all sellers
    except Buyers.DoesNotExist:
        buyer = None
        profile_type = 'seller'
        seller_details = Sellers.objects.filter(user=user)  # If the user is a seller, show only their details

    context = {
        'user': user,
        'profile_type': profile_type,
        'buyer': buyer,
        'seller_details': seller_details,
    }
    return render(request, 'profile.html', context)

