from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('users', views.getUsers, name='get_all_users'),
    path('users/<int:id>', views.getUserById, name='get_user'),
    path('users/create', views.createUser, name='create_user'),
    path('users/update/<int:id>', views.updateUser, name='update_user'),
    path('users/delete/<int:id>', views.deleteUser, name='delete_user'),
    
    path('clients', views.getClients, name='get_all_clients'),
    path('clients/<int:id>', views.getClient, name='get_client'),
    path('clients/create', views.createClient, name='create_client'),
    path('clients/update/<int:id>', views.updateClient, name='update_client'),
    path('clients/delete/<int:id>', views.deleteClient, name='delete_client')
]
