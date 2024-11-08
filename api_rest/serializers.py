from rest_framework import serializers

from .models import User 
from .models import Client 
from .models import Product 

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'

class ClientSerializer(serializers.ModelSerializer):
  class Meta:
    model = Client
    fields = '__all__'
    
class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = '__all__'