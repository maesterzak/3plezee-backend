from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *



class ContactUsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ContactUs
        fields = "__all__"

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields = "__all__"


class CustomerSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)
    class Meta:
        model = Customer
        fields = ['first_name','last_name','state', 'city', 'country', 'address', 'postal_code', 'phone_number']


class OrderItemsSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderItem
        fields = "__all__"



class OrderSerializer(serializers.ModelSerializer):
    customer = CustomerSerializer(read_only=True, many=False)
    order_items = OrderItemsSerializer(read_only=True, many=True)
    class Meta:
        model = Order
        fields = ["status", "order_id", "date_ordered", "complete_customer", "complete_Seller", "payment_method", "confirm_payment", "order_items", "shipping_address", "quantity", "postal_code", "phone_number", "total", "customer"]

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = "__all__"

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImages
        fields = "__all__"

class AttributesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attributes
        fields = "__all__"

class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = "__all__"        

class ProductSerializer(serializers.ModelSerializer):
    # user = UserSerializer(read_only=True)
    product_attribute = AttributesSerializer(many = True, read_only=True)
    product_image = ProductImageSerializer(many=True, read_only=True)
    product_ratings = RatingSerializer(many=True, read_only=True)
    category = CategorySerializer(many=False, read_only=True)
  
    class Meta:
        model = Product
        fields = ("name", "slug", "price", "category", "description", "stock", "product_attribute", "product_image",  "product_ratings", "id")

