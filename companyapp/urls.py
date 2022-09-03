from django.urls import path
from companyapp import views

urlpatterns = [
    path('signup/',views.company_signup,name='company_signup'),
    path('signin/',views.company_signin,name='company_signin'),
    path('<int:cid>',views.company_home,name='companyhome'),
    #path('addproduct/<int:cid>',views.addproduct,name='addproduct'),
    path('addproduct/<int:cid>',views.addproductform,name='addproduct'),
    path('profile/<int:cid>',views.company_profile,name='company_profile'),
    path('edit_company/<int:cid>',views.edit_company,name='edit_company'),
    path('edit_product/<int:productid>/',views.edit_product,name='edit_product'),
]