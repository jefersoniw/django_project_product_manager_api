from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('users', views.getUsers, name='get_all_users'),
    path('users/<int:id>', views.getUserById, name='get_user'),
    path('users/create', views.createUser)
]
