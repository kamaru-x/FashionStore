from django.urls import path
from userapp import views

urlpatterns = [
    path('',views.home,name='home'),
    path('signup/',views.signup,name='signup'),
    path('signin/',views.signin,name='signin'),
    path('<int:userid>',views.logged_home,name='logged_home'),
    path('shop/<int:userid>',views.shop,name='shop'),
    path('details/<int:userid>/<int:productid>/',views.details,name='details'),
    path('profile/<int:userid>',views.profile,name='profile'),
    path('edit_profile/<int:userid>',views.edit_profile,name='edit_profile'),
    path('cart/<int:userid>',views.cart,name='cart'),
    path('placeorder/<int:userid>/',views.placeorder,name='placeorder'),
    path('remove/<int:cartid>/',views.remove,name='remove')
]