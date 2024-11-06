from rest_framework import serializers

from .models import User 
from .models import Client 
from .models import Product 

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['id', 'name', 'email', 'created_at', 'updated_at']

class ClientSerializer(serializers.ModelSerializer):
  class Meta:
    model = Client
    fields = '__all__'
    
class ProductSerializer(serializers.ModelSerializer):
  class Meta:
    model = Product
    fields = '__all__'