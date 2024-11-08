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

#USERS
@api_view(['GET'])
def getUsers(request):
  if request.method == 'GET':
    users = User.objects.all()
    
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)
  
  return Response('Erro!', status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getUserById(request, id):
  try:
    user = User.objects.get(pk=id)
  except:
    return Response('Not Found!', status=status.HTTP_404_NOT_FOUND)
  
  if request.method == 'GET':    
    serializer = UserSerializer(user)
    return Response(serializer.data)
  
@api_view(['POST'])
def createUser(request):
  if request.method == 'POST':
    
    try: 
      serializer = UserSerializer(data=request.data)
      
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except:
      return Response('Erro!', status=status.HTTP_400_BAD_REQUEST)
    
    return Response('Erro!', status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['PUT'])
def updateUser(request, id):
    
  if request.method == 'PUT':         
    try:
      user = User.objects.get(pk=id)
    except:
      return Response('Not Found!', status=status.HTTP_404_NOT_FOUND)
    
    serializer = UserSerializer(user, data=request.data)
    
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
    
    return Response('Erro!', status=status.HTTP_400_BAD_REQUEST)
  
@api_view(['DELETE'])
def deleteUser(request, id):
  
  if request.method == 'DELETE':
    try: 
      user = User.objects.get(pk=id)
    except:
      return Response('Not Found!', status=status.HTTP_404_NOT_FOUND)
    
    user.delete()
    return Response('User Deleted!', status=status.HTTP_202_ACCEPTED)
    
  return Response('Erro!', status=status.HTTP_400_BAD_REQUEST) 

#CLIENTS
@api_view(['GET'])
def getClients(request):
  if request.method == 'GET':
    
    clients = Client.objects.all()
    
    serializer = ClientSerializer(clients, many=True)
    return Response(serializer.data)
  
  return Response('Erro!', status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getClient(request, id):
  if request.method == 'GET':
    
    try:
      client = Client.objects.get(pk=id)
    except:
      return Response('Not found!', status=status.HTTP_404_NOT_FOUND)
    
    serializer = ClientSerializer(client)
    return Response(serializer.data)
  
  return Response('Erro!', status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def createClient(request):
  if request.method == 'POST':
    
    serializer = ClientSerializer(data=request.data)
    try:
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
    except:
      return Response('Erro!', status=status.HTTP_400_BAD_REQUEST)
    
  return Response('Erro!', status=status.HTTP_400_BAD_REQUEST) 

@api_view(['PUT'])
def updateClient(request, id):
  if request.method == 'PUT':
    
    try:
      client = Client.objects.get(pk=id)
    except:
      return Response('Not found!', status=status.HTTP_404_NOT_FOUND)
    
    serializer = ClientSerializer(client, data=request.data)
    
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

  return Response('Erro!', status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteClient(request, id):
  if request.method == 'DELETE':
    
    try:
      client = Client.objects.get(pk=id)
    except:
      return Response('Not found!', status=status.HTTP_404_NOT_FOUND)
    
    client.delete()
    return Response('Client Deleted!', status=status.HTTP_202_ACCEPTED)
    
  return Response('Erro!', status=status.HTTP_400_BAD_REQUEST) 
    
# PRODUCTS
@api_view(['GET'])
def getProducts(request):
  if request.method == 'GET':
    
    products = Product.objects.all()
    
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)
  
  return Response('Erro!', status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getProduct(request, id):
  if request.method == 'GET':
    
    try:
      product = Product.objects.get(pk=id)
    except:
      return Response('Not found!', status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProductSerializer(product)
    return Response(serializer.data)
  
  return Response('Erro!', status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def createProduct(request):
  if request.method == 'POST':
    
    serializer = ProductSerializer(data=request.data)
    try:
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)
    except:
      return Response('Erro!', status=status.HTTP_400_BAD_REQUEST)
    
  return Response('Erro!', status=status.HTTP_400_BAD_REQUEST) 

@api_view(['PUT'])
def updateProduct(request, id):
  if request.method == 'PUT':
        
    try:
      product = Product.objects.get(pk=id)
    except:
      return Response('Not found!', status=status.HTTP_404_NOT_FOUND)
    
    serializer = ProductSerializer(product, data=request.data)
    
    print(serializer.is_valid())
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

  return Response('Erro!', status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteProduct(request, id):
  if request.method == 'DELETE':
    
    try:
      product = Product.objects.get(pk=id)
    except:
      return Response('Not found!', status=status.HTTP_404_NOT_FOUND)
    
    product.delete()
    return Response('Product Deleted!', status=status.HTTP_202_ACCEPTED)
    
  return Response('Erro!', status=status.HTTP_400_BAD_REQUEST) 