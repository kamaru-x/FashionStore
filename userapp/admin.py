from django.contrib import admin
from userapp.models import User,Cart,Order
# Register your models here.

admin.site.register(User)
admin.site.register(Cart)
admin.site.register(Order)