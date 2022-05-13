from django.contrib import admin
from .models import Category, Sub_Category,Brand,Product,Banner,Profile,Order

# Register your models here.


admin.site.register(Category)
admin.site.register(Sub_Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Banner)
admin.site.register(Profile)
admin.site.register(Order)
