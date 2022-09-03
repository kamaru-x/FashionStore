from django import forms
from companyapp.models import Product,Company

class Product_form(forms.ModelForm):
    class Meta():
        model = Product
        fields = '__all__'

class Company_update(forms.ModelForm):
    class Meta():
        model = Company
        fields = '__all__'