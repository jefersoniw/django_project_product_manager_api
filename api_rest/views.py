from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

import logging
import pdb

from .models import User
from .serializers import UserSerializer

from .models import Client
from .serializers import ClientSerializer

from .models import Product
from .serializers import ProductSerializer

import json


@api_view(['GET'])
def getUsers(request):
  if request.method == 'GET':
    users = User.objects.all()
    
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
  
  return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getUserById(request, id):
  try:
    user = User.objects.get(pk=id)
  except:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':    
    serializer = UserSerializer(user)
    return Response(serializer.data)
  
@api_view(['POST'])
def createUser(request):
  if request.method == 'POST':
    
    user = request.data 
    serializer = UserSerializer(data=user)
    
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(status=status.HTTP_400_BAD_REQUEST)