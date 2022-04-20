from django.db import models
from django.contrib.auth.models import User

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
    
class Banner(models.Model):
     heading=models.CharField(max_length=200)
     sub_heading=models.CharField(max_length=200)
     short_description=models.TextField()
     image=models.ImageField(upload_to='static/bannerImg')
     def __str__(self):
            return self.heading 
             
class Profile(models.Model):
      user = models.OneToOneField(User, on_delete=models.CASCADE )
      fullname =models.CharField(max_length=150)
      nickname =models.CharField(max_length=150)
      phone_number =models.CharField(max_length=10)
      second_number =models.CharField(max_length=10)
      disctrict =models.CharField(max_length=150)
      city =models.CharField(max_length=150)
      local_area =models.CharField(max_length=150)
      house_number =models.CharField(max_length=150)
      birthday =models.DateField( help_text = "User birthdate")
      gender =models.CharField(max_length=150)
      profile_picture =models.ImageField(upload_to='static/profileImage')
      
      def __str__(self):
            return self.fullname 
      
      def age(self):
        import datetime
        return int((datetime.date.today() - self.birthday).days / 365.25  )
