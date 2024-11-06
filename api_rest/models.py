from django.db import models

# Create your models here.
#model User
class User(models.Model):
  name = models.CharField(max_length=100)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=15)
  
  def __str__(self):
    return f'Name: {self.name} | Email: {self.email}'
  
#model Client
class Client(models.Model):
  SEX_CHOICES = [
    ('M', 'Masculino')
    ('F', 'Feminino')
    ('O', 'Outros')
  ]
  
  name = models.CharField(max_length=100)
  cpf = models.CharField(max_length=11, unique=True)
  address = models.CharField(max_length=255)
  sex = models.CharField(max_length=1, choices=SEX_CHOICES)
  created_at = models.DateTimeField(auto_now=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f'Name: {self.name} | CPF: {self.cpf}'
  
#model Product
class Product(models.Model):  
  name = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  client = models.models.ForeignKey(Client, on_delete=models.CASCADE, related_name="products")
  created_at = models.DateTimeField(auto_now=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  
  def __str__(self):
    return f'Product: {self.name}'
  