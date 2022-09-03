from django.db import models

# Create your models here.

from companyapp.models import Product

class User(models.Model):
    Name = models.CharField(max_length=25)
    Email = models.EmailField()
    Password = models.CharField(max_length=20)

    def __str__(self):
        return self.Name   

class Cart(models.Model):
    User_id = models.ForeignKey(User,on_delete=models.CASCADE)
    Product_id = models.ForeignKey(Product,on_delete=models.CASCADE)


class Order(models.Model):
    User_id = models.ForeignKey(User,on_delete=models.CASCADE)
    Product_id = models.ForeignKey(Product,on_delete=models.CASCADE)
    Name = models.CharField(max_length=35)
    Phone = models.CharField(max_length=15)
    Place = models.CharField(max_length=35)
    Pincode = models.IntegerField()
    Address = models.TextField()