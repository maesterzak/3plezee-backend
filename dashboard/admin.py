from django.contrib import admin
from .models import *
import re
# Register your models here.


class AttributeAdmin(admin.StackedInline):
    model = Attributes
    
    extra = 0

    # def has_add_permission(self, request, order):
    #     return False

class ProductImageAdmin(admin.StackedInline):
    model = ProductImages
    
    extra = 0

    # def has_add_permission(self, request, order):
    #     return False

class ProductAdmin(admin.ModelAdmin):
    search_fields = ["name__startswith"]
    
    inlines =  [
        ProductImageAdmin,AttributeAdmin
    ]   

    
    exclude = ['slug']        

class OrderItemsAdmin(admin.StackedInline):
    model = OrderItem
    exclude = ['date_added']
    extra = 0

    def has_add_permission(self, request, order):
        return False

class OrderAdmin(admin.ModelAdmin):
    search_fields = ["order_id__startswith"]
    list_filter = ['complete_Seller']
    list_display = ('customer', 'order_id', 'status', 'complete_Seller', 'date_ordered')
    inlines =  [
        OrderItemsAdmin
    ]
    
class CategoryAdmin(admin.ModelAdmin):
    model = Category
    exclude = ['slug']    


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
admin.site.register(ProductImages)
admin.site.register(Rating)
admin.site.register(Attributes)
admin.site.register(Customer)
admin.site.register(ContactUs)
