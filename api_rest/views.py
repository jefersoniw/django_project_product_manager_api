from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

from .models import Client
from .serializers import ClientSerializer

from .models import Product
from .serializers import ProductSerializer

import json