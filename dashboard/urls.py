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

    # path('all-posts/', all_posts, name='posts'),
    # path('posts/', posts, name='posts_paginated'),
    # path('post-detail/<str:pk>/', post_detail, name='post_detail'),
    # # path('post-create/', post_create, name='post_create'),
    # # path('post-update/<str:pk>/', post_update, name='post_update'),
    # # path('post-delete/<str:pk>/', post_delete, name='post_delete'),
    # path('categories/', all_categories, name='categories-list'),
    # path('search/', blog_search, name='blog_search'),
    # path('category-posts/<str:str>/', all_category_paginated_post, name='category_p_post'),
    # path('threads/', threads, name='threads'),
    # path('all-threads/', all_threads, name='all_threads'),
    # path('thread-detail/<str:pk>/', thread_detail, name='thread_detail'),
    # path('thread-create/', thread_create, name='thread_create'),
    # path('message-create/', message_create, name='message_create'),
    # path('comment-create/', comment_create, name='comment_create'),
    # path('register/', register.as_view(), name='register'),
    # path('user/', loaduserview.as_view(), name='user'),
    # path('portfolio-skill/', all_portfolio_skills, name='portfolio_skill'),
    # path('portfolio-projects/', all_portfolio_projects, name='portfolio_projects'),

]