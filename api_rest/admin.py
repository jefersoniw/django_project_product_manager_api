from django.contrib import admin

# Register your models here.
from .models import User, Client, Product

admin.site.register(User)
admin.site.register(Client)
admin.site.register(Product)