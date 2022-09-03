from django.contrib import admin
from companyapp.models import Category,Company,Product
# Register your models here.

admin.site.register(Company)
admin.site.register(Category)
admin.site.register(Product)