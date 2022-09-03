from itertools import product
from django.shortcuts import render,redirect
from companyapp.models import Category,Company,Product
from django.contrib import messages
from companyapp.forms import Company_update,Product_form
# Create your views here.

def company_signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        company = Company.objects.filter(Email=email).exists()

        if company:
            messages.warning(request,'email already exists')
            return redirect('company_signup')
        elif password1 != password2 :
            messages.warning(request,'password does not match')
            return redirect('company_signup')
        else:
            companydata = Company(Name=name,Email=email,Password=password1)
            companydata.save()
            return redirect('/company/%s' %companydata.id)
    return render(request,'company_signup.html')

####################################################################

def company_signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        company = Company.objects.filter(Email=email).exists()

        if not company:
            messages.warning(request,'incorrect email')
            return redirect('company_signin')
        elif password != (Company.objects.get(Email=email)).Password :
            messages.warning(request,'incorrect password')
            return redirect('company_signin')
        else :
            companydata = Company.objects.get(Email=email)
            return redirect('/company/%s' %companydata.id)
    return render(request,'company_signin.html')

####################################################################

def company_home(request,cid):
    company = Company.objects.get(id=cid)
    products = Product.objects.filter(Company = company.id)
    
    return render(request,'company_home.html',{'company':company,'products':products})

####################################################################

def addproduct(request,cid):
    categories = Category.objects.all()
    company = Company.objects.get(id=cid)
    if request.method == 'POST':
        name = request.POST.get('p_name')
        category = request.POST.get('category')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES['image']       
        company = Company.objects.get(id=cid)
        productdata = Product(Name=name,Category=category,Price=price,Description=description,Image=image)
        productdata.save()
        return redirect('/company/%s' % company.id)
    return render (request,'addproduct.html',{'company':company,'categories':categories})

#####################################################################

def company_profile(request,cid):
    company = Company.objects.get(id=cid)
    return render(request,'company_profile.html',{'company':company})

#####################################################################

def edit_company(request,cid):
    data = Company.objects.get(id=cid)
    if request.method == 'POST':
        form = Company_update(request.POST or None,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/company/%s'% data.id)
    else:
        form = Company_update(request.POST or None,instance=data)
    return render(request,'edit_company.html',{'form':form})

#####################################################################

def edit_product(request,productid):
    data = Product.objects.get(id=productid)
    if request.method == 'POST':
        form = Product_form(request.POST or None,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/company/%s' % data.id)
    else:
        form = Product_form(request.POST or None,instance=data)
    return render(request,'edit_product.html',{'form':form})

#####################################################################

def addproductform(request,cid):
    company = Company.objects.get(id=cid)
    if request.method == 'POST' :
        form = Product_form(request.POST or None , request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('/company/%s' % company.id)
    else:
        form = Product_form()
    return render(request,'addproductform.html',{'company':company,'form':form})
