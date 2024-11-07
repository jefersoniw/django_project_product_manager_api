from django.db import models

# Create your models here.

#model base para definições de criação e atualizaçãoi de registros
class Base(models.Model):
  created_at = models.DateTimeField(auto_now=True)
  updated_at = models.DateTimeField(auto_now_add=True)
  
  class Meta:
    abstract = True

#model User
class User(Base):
  name = models.CharField(max_length=100)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=15)
  
  class Meta:
    verbose_name = 'User'
    verbose_name_plural = 'Users'
  
  def __str__(self):
    return f'Name: {self.name}'
  
#model Client
class Client(Base):  
  name = models.CharField(max_length=100)
  cpf = models.CharField(max_length=11, unique=True)
  address = models.CharField(max_length=255)
  sex = models.CharField(max_length=1)
  
  class Meta:
    verbose_name = 'Client'
    verbose_name_plural = 'Clients'
  
  def __str__(self):
    return f'Name: {self.name} | CPF: {self.cpf}'
  
#model Product
class Product(Base):  
  name = models.CharField(max_length=100)
  price = models.DecimalField(max_digits=10, decimal_places=2)
  client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="products")
  
  class Meta:
    verbose_name = 'Product'
    verbose_name_plural = 'Products'
  
  def __str__(self):
    return f'Product: {self.name}'
  