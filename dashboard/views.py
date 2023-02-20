from django.shortcuts import render
from .serializer import *
from rest_framework import permissions, status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
import random
import datetime


# Create your views here.


@api_view(['PATCH', 'GET'])
@permission_classes([IsAuthenticated])
def profile(request):
    customer = Customer.objects.get(email = request.user.email)
    
    if customer.user is None:
        customer.user = request.user
        customer.save()
    print('nb', request.data)
    if request.method == "PATCH":
        
        serializer = CustomerSerializer(customer, data=request.data, partial=True)
        print("ser", serializer)
        if serializer.is_valid():
            
            serializer.save()
        else:
            print(serializer.errors)    
        
        return Response(
            {'data':serializer.data},
                                status = status.HTTP_200_OK)
    elif request.method == "GET":
        
        serializer = CustomerSerializer(customer)
        return Response(
            {'data':serializer.data},
                                status = status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_order(request):
    customer = Customer.objects.get(email = request.user.email)
    data = request.data
    print("sdd", data)
    shipping_det = data['shipping_det']
    address = f"{shipping_det['address']} {shipping_det['city']} {shipping_det['state']}, {shipping_det['country']}"
    order_id = f"3PZ{random.randint(111111, 91111111)}{customer.id}"
    order = Order.objects.create(order_id=order_id, customer=customer, payment_method=data['payment_method'], shipping_address=address, postal_code=shipping_det['postal_code'], phone_number=shipping_det['phone_number'], total=data['total'], quantity=data['quantity'])
    for x in data['cart']:
        product = Product.objects.get(slug=x['slug'])
        OrderItem.objects.create(quantity=x['quantity'], order=order, product_name=product.name, product_price=product.price, product_attribute=x['attributes'], product_image=x['image'])

    return Response(
        {'data': order_id},
                            status = status.HTTP_200_OK)
        


@api_view(['PATCH', 'GET'])
@permission_classes([IsAuthenticated])
def order(request, slug):
    
    print('nb', slug)
    if request.method == "PATCH":
        order = Order.objects.get(order_id = slug)
        serializer = OrderSerializer(order, data=request.data, partial=True)
        if serializer.is_valid():
            
            serializer.save()
        
        return Response(
            {'data':serializer.data},
                                status = status.HTTP_200_OK)
    elif request.method == "GET":
        order = Order.objects.get(order_id = slug)
        
        serializer = OrderSerializer(order)
        return Response(
            {'data':serializer.data},
                                status = status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def orders(request):
    customer = Customer.objects.get(email = request.user.email)
    orders = Order.objects.filter(customer=customer)
    serializer = OrderSerializer(orders, many=True)

    return Response(
            {'data':serializer.data}, 
                                status = status.HTTP_200_OK)   

@api_view(['POST'])
# @permission_classes([IsAuthenticated])
def confirm_order(request):
    data = request.data
    out_of_stock = []
    for x in data:
        try:
           item = Product.objects.get(slug = x["slug"], price = x['price'], stock__gt=0)
        except:
            out_of_stock.append(x["name"])
        
    return Response(
            {'data': out_of_stock},
                                status = status.HTTP_200_OK)


@api_view(['GET'])
def categories(request):
    categories= Category.objects.all()
    serializer = CategorySerializer(categories, many=True)

    return Response(
            {'data':serializer.data},
                                status = status.HTTP_200_OK)


@api_view(['GET'])
def category(request, slug):
    category= Category.objects.get(slug = slug)
    
    products = Product.objects.filter(category=category)

    serializer = ProductSerializer(products, many=True, read_only=True)
    
    return Response(
            {'category':'catgeory','products':serializer.data},
                                status = status.HTTP_200_OK)

@api_view(['GET'])
def latest_products(request):
    products = Product.objects.all().order_by('-id')[:6]
    serializer = ProductSerializer(products, many=True, read_only=True)
    
    return Response(
            {'data':serializer.data},
                                status = status.HTTP_200_OK)


@api_view(['GET'])
def products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True, read_only=True)
    
    return Response(
            {'data':serializer.data},
                                status = status.HTTP_200_OK)


@api_view(['GET'])
def product(request, slug):
    
    product= Product.objects.get(slug = slug)
    serializer = ProductSerializer(product, read_only=True, many=False)

    products_similar = Product.objects.filter(category=product.category).exclude(name=product.name)
    
    similar_products = [*products_similar]
    
    dataLength = len(products_similar)
    
    if dataLength > 4:
        similar_products = random.sample(similar_products, k=4)
    else:
        similar_products = random.sample(similar_products, k=dataLength)
    serializer2 = ProductSerializer(similar_products, many=True, read_only=True)
   
    return Response(
            {'product':serializer.data, 'similar_products': serializer2.data},
                                status = status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def rating(request):
    serializer = RatingSerializer(data=request.data)
  
    if serializer.is_valid():

        serializer.save()
        product = Product()
        return Response(
            {'data':serializer.data},
                                status = status.HTTP_201_CREATED)
    else:
        
        return Response(
        status = status.HTTP_500_INTERNAL_SERVER_ERROR)                            
    


