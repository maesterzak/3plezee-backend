from django.urls import path
from .views import *



app_name = "dashboard"
urlpatterns = [
    #profile
    path('profile/', profile, name='profile'),
    
    #catgeory
    path('categories/', categories, name='categories'),
    path('category/<slug:slug>/', category, name='category'),
    #products
    path('latest-products/', latest_products, name='latest_products'),
    path('products/', products, name='products'),
    path('product/<slug:slug>/', product, name='product'),
    #rating
    path('rating/', rating, name='rating'),

    #order
    path('orders/', orders, name='orders'),
    path('order/<slug:slug>/', order, name='order'),
    path('confirm-order/', confirm_order, name='confirm_order'),
    path('create-order/', create_order, name='create_order'),

    #contact us
    path('contact-us/', contact_us, name='contact_us'),
]