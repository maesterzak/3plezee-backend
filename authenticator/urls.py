from django.urls import path
from .views import *



app_name = "authenticator"
urlpatterns = [
    path('dj-rest-auth/google/', GoogleLogin.as_view(), name='google_login')

]