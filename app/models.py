from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=150)
    
    def __str__(self):
            return self.name
    
class Sub_Category(models.Model):
    name =models.CharField(max_length=150)
    category =models.ForeignKey(Category, on_delete=models.CASCADE)  
      
    def __str__(self):
            return self.name
     
class Brand(models.Model):
    name=models.CharField(max_length=150)   
    def __str__(self):
            return self.name

class Product(models.Model):
    name =models.CharField(max_length=150)
    price=models.IntegerField()
    rentalprice=models.IntegerField()
    image =models.ImageField(upload_to='static/productImg')
    date =models.DateField(auto_now_add=True)
    category =models.ForeignKey(Category, on_delete=models.CASCADE,default=None)  
    sub_category = models.ForeignKey(Sub_Category, on_delete=models.CASCADE, default=None) 
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=None) 
    
    def __str__(self):
            return self.name
         
    