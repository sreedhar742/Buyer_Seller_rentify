from django.contrib import admin

# Register your models here.
from .models import Buyers,Sellers


admin.site.register(Buyers)
admin.site.register(Sellers)