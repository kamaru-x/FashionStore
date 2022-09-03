from django.db import models

# Create your models here.

class Company(models.Model):
    Name = models.CharField(max_length=25)
    Email = models.EmailField()
    Password = models.CharField(max_length=20)

    def __str__(self):
        return self.Name   

class Category(models.Model):
    Name = models.CharField(max_length=25)
    Slug = models.SlugField()

    class Meta:
        ordering =('Name',)

    def __str__(self):
        return self.Name

class Product(models.Model):
    Name = models.CharField(max_length=25)
    Catagory = models.ForeignKey(Category,on_delete=models.CASCADE)
    Company = models.ForeignKey(Company,on_delete=models.CASCADE)
    Slug = models.SlugField()
    Description = models.TextField()
    Price = models.IntegerField()
    Image = models.ImageField(upload_to = 'uploades/')
    Created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering =('-Created_at',)

    def __str__(self):
        return self.Name