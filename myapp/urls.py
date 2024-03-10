from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   #path('admin/', admin.site.urls),
    path('hello1/', hello1, name='hello'),
path('',projecthome, name='projecthome'),
    path('buyerhome/',myhome, name='myhome'),
path('signup',signup, name='signup'),
path('signup1',signup1, name='signup1'),
path('login',login, name='login'),
path('login1',login1, name='login1'),
path('logout',logout, name='logout'),
    path('sellerhome/', sellerhome, name='sellerhome'),
     path('deals/',mydeals, name='mydeals'),
    path('feedback', feedback, name='feedback'),
path('feedback1', feedback1, name='feedback1'),
path('thank_you', thank_you, name='thank_you'),
path('addproducts/',addproducts, name='addproducts'),
path('add_details/',add_details, name='add_details'),
path('viewsellerproducts/',view_seller_products, name='view_seller_products'),
path('viewproducts/',viewproducts, name='viewproducts'),
    path('skin/', skincare, name='skincare'),
path('makeup/', makeup, name='makeup'),
path('fragrance/', fragrance, name='fragrance'),
path('buynow/',buynow, name='buynow'),

    path('cart/', cart, name='cart'),


    ]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
