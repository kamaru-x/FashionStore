from django.shortcuts import render,redirect
from userapp.models import Order, User,Cart
from companyapp.models import Product,Category,Company
from django.contrib import messages
from django.db.models import Q
# Create your views here.

def signup(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        user = User.objects.filter(Email=email).exists()

        if user:
            messages.warning(request,'email already exists')
            return redirect('signup')
        elif password1 != password2:
            messages.warning(request,'password does not match')
            return redirect('signup')
        else:
            data = User(Name=name,Email=email,Password=password1)
            data.save()
            userdata = User.objects.get(Email=email)
            return redirect('/%s' %userdata.id)
    return render(request,'signup.html')

####################################################################

def signin(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.filter(Email=email).exists()

        if not user:
            messages.warning(request,'invalid email address')
            return redirect('signin')
        elif password != (User.objects.get(Email=email)).Password:
            messages.warning(request,'incorrect password')
            return redirect('signin')
        else:
            userdata = User.objects.get(Email=email)
            return redirect('/%s' %userdata.id)
    return render(request,'signin.html')

####################################################################

def home(request):
    products = Product.objects.all()
    return render(request,'default.html',{'products':products})

####################################################################

def logged_home(request,userid):
    products = Product.objects.all()
    logged_user = User.objects.get(id=userid)
    return render(request,'userhome.html',{'products':products,'logged_user':logged_user})

####################################################################

def shop(request,userid):
    products = Product.objects.all()
    categories = Category.objects.all()
    logged_user = User.objects.get(id=userid)

    active_category = request.GET.get('category','')

    if active_category:
        products = products.filter(Slug = active_category)

    query = request.GET.get('query','')
    if query:
        products = products.filter(Q(Name__icontain=query) | Q(Description__icontain=query))

    context = {
        'products':products,
        'categories':categories,
        'active_category':active_category,
        'logged_user':logged_user,
    }
    return render(request,'usershop.html',context)

####################################################################

def details(request,userid,productid):
    logged_user = User.objects.get(id=userid)
    product = Product.objects.get(id=productid)

    context = {
        'product':product,
        'logged_user':logged_user,
    }
    return render(request,'details.html',context)

#####################################################################

def profile(request,userid):
    logged_user = User.objects.get(id=userid)
    return render(request,'profile.html',{'logged_user':logged_user})

#####################################################################

def edit_profile(request,userid):
    logged_user = User.objects.get(id=userid)
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')

        data = User(Name=name,Email=email)
        data.save()
        return redirect('profile/%s' % logged_user.id)
    return render(request,'edit_profile.html',{'logged_user':logged_user})

#####################################################################

def cart(request,userid):
    logged_user = User.objects.get(id=userid)
    cartdata = Cart.objects.filter(User_id=logged_user.id)
    if request.method == 'POST':
        product = request.POST.get('product')
        user = logged_user.id
        pro = Product.objects.get(id=product)
        usr = User.objects.get(id=user)
        data = Cart(User_id=usr,Product_id=pro)
        if not Cart.objects.filter(User_id=usr,Product_id=pro).exists():
            data.save()
        else:
            pass
        return render(request,'cart.html',{'logged_user':logged_user,'items':cartdata})
    return render(request,'cart.html',{'logged_user':logged_user,'items':cartdata})

##########################################################################

def placeorder(request,userid):
    logged_user = User.objects.get(id=userid)
    delete_data = Cart.objects.all()
    delete_data.delete()
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        place = request.POST.get('place')
        pincode = request.POST.get('pincode')
        address = request.POST.get('address')
        product = Cart.objects.get(User_id=userid)
        user = logged_user.id
        pro = Product.objects.get(id=product)
        usr = User.objects.get(id=user)

        orderdata = Order(User_id=usr,Product_id=pro,Name=name,Phone=phone,Place=place,Pincode=pincode,Address=address)
        orderdata.save()
        delete_data = Cart.objects.all()
        delete_data.delete()
    return render(request,'placeorder.html',{'logged_user':logged_user})

##########################################################################

def remove(request,cartid):
    data = Cart.objects.get(id=cartid)
    data.delete()
    return redirect('/')