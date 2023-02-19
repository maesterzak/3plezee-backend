from django.shortcuts import render
# from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from .SocialLogin import GoogleOAuth2Adapter

# class GoogleLogin(SocialLoginView): # if you want to use Authorization Code Grant, use this
#     adapter_class = GoogleOAuth2Adapter
#     callback_url = "http://localhost:8000/accounts/google/login/callback/" #CALLBACK_URL_YOU_SET_ON_GOOGLE
#     client_class = OAuth2Client

class GoogleLogin(SocialLoginView):
  authentication_classes = [] # disable authentication, make sure to override `allowed origins` in settings.py in production!
  adapter_class = GoogleOAuth2Adapter
  callback_url = "http://localhost:8000/accounts/google/login/callback/" #"http://localhost:3000"  # frontend application url
  client_class = OAuth2Client




class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter