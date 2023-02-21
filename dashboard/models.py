from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField
import re
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        title = self.name.lower()
        x = ['@', '#', '?', "/", ".", ",", "&", "!","|","-","_"]
        z ="".join(filter(lambda char: char not in x, title)) 
        self.slug = re.sub(r"\s+", '-', z)
        super().save(*args, **kwargs)    

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    first_name = models.CharField(max_length=200, null=True)
    last_name = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    postal_code = models.CharField(max_length=20, null=True, blank=True)
    phone_number = models.CharField(max_length=11)    
    email = models.EmailField()
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.user)



class Product(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, blank=True, null=True, related_name="category")
    description = models.TextField()
    stock = models.IntegerField()

    

    def __str__(self):
        return str(self.name)

    def save(self, *args, **kwargs):
        title = self.name.lower()
        x = ['@', '#', '?', "/", ".", ",", "&", "!","|","-","_"]
        z ="".join(filter(lambda char: char not in x, title)) 
        self.slug = re.sub(r"\s+", '-', z)
        super().save(*args, **kwargs)    


class Attributes(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_attribute', null=True)
    name = models.CharField(max_length=50)
    value = ArrayField(models.CharField(null=False, blank=True, max_length=50), default=list, blank=True)    
    
    def __str__(self):
        return str(self.name)

class ProductImages(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_image', null=True)
    name = models.CharField(max_length=40)
    image = models.ImageField()
   
    def __str__(self):
        return str(self.name)

    


class Rating(models.Model):
    product = models.ForeignKey(Product, related_name='product_ratings', on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100,  null=True)
    rating = models.FloatField()
    message = models.TextField()

    def __str__(self):
        return str(self.name)


class Order(models.Model):
    STATUS_CHOICES = (
        ('pending', 'pending'),
        ('on_route', 'on_route'),
        ('delivered', 'delivered'),
        ('completed', 'completed')
    )
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, blank=True, null=True,)
    date_ordered = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        'Status',
        max_length=20,
        choices=STATUS_CHOICES,
        default='pending')
    order_id = models.CharField(max_length=200, null=True)
    transaction_ref = models.CharField(max_length=500, null=True)
    complete_customer = models.BooleanField(default=False, null=True, blank=False)
    complete_Seller = models.BooleanField(default=False)
    payment_method=models.CharField(max_length=30, blank=False)
    confirm_payment = models.BooleanField(default=False, null=True)
    total = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    shipping_address = models.CharField(max_length=1000, null=True)
    postal_code = models.CharField(max_length=100, null=True)
    phone_number = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.customer)   

     

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_order_total(self):
        orderitemsstuff = self.orderitemsstuff_set.all()
        total = sum([orderitemsstuff.total for orderitemsstuff in orderitemsstuff])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    



class OrderItem(models.Model):
    
    order = models.ForeignKey(Order, related_name="order_items" ,on_delete=models.CASCADE, blank=True, null=True, )
    product_name = models.CharField(max_length=200, default='unknown')
    product_price = models.IntegerField(default=0)
    product_attribute = models.CharField(max_length=200 , default='unknown')
    product_image = models.CharField(max_length=500, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.order)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ContactUs(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    phone_number = models.CharField(max_length=50)
    message = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)



class NewsLetter(models.Model):
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.email)
