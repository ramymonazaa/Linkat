from distutils.command.upload import upload
from django.db import models
from turtle import title
# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(blank=True,null=True)
    def __str__(self):
        return self.name
        
class Product(models.Model):
    id= models.AutoField(primary_key=True)
    name=models.CharField(max_length=100,default='undefiend',unique=True)
    email=models.CharField(null=True,max_length=100)
    description=models.TextField(blank=True,null=True)
    rate=models.IntegerField(default=0,null=True)
    category=models.ForeignKey(Category,default=True,null=False,on_delete=models.CASCADE)
    image= models.ImageField(upload_to='media/%y/%m/%d',null=True,blank=True)
    state=models.IntegerField(default=1)
    owner=models.CharField(max_length=100,default='LINKY')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name='Link'
        ordering=['-rate','name']

class User(models.Model):
    username=models.CharField(max_length=100)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=12)
    fav_products=models.ManyToManyField(Product,null=True,blank=True)
    num_visits=models.IntegerField(default=0)
    points=models.IntegerField(default=0)
    image= models.ImageField(upload_to='media/%y/%m/%d',null=True,blank=True)
    
    def __str__(self):
        return self.username
    class Meta:
        verbose_name='user'
        ordering=['-points','username']
