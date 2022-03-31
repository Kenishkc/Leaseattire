
from django.shortcuts import render ,redirect
from app.models import  Category,Brand,Product,Banner,Sub_Category
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login




# Create your views here.
def master(request):
    brands=Brand.objects.all()
    banner=Banner.objects.all()
    category= Category.objects.all()
  
    
    categoryID=request.GET.get('category')
    if categoryID:
       product =Product.objects.filter(sub_category=categoryID)       
    else:
         product=Product.objects.all()
    
    brandId=request.GET.get('brand')
    if brandId:
         product =Product.objects.filter(brand=brandId)
        
    subcategory=Sub_Category.objects.filter(category='1')
    
    sub_product =Product.objects.filter(category='1')
    
        
        
    context={
        'category':category,
        'brand':brands,
        'product':product,
        'banner':banner,
        'subcategory':subcategory,
        'subproduct':sub_product,
        
    }
    return render(request, 'index.html',context)

def productDetails(request, id):
    product =Product.objects.filter(id=id).first()
    context={
        
        'product':product,
      
    }
    
    return render(request, 'productDetails.html',context)

def shop(request):
    brands=Brand.objects.all()
    banner=Banner.objects.all()
    category= Category.objects.all()
  
    
    categoryID=request.GET.get('category')
    if categoryID:
       product =Product.objects.filter(sub_category=categoryID)       
    else:
         product=Product.objects.all()
    
    brandId=request.GET.get('brand')
    if brandId:
         product =Product.objects.filter(brand=brandId)
        
    
        
        
    context={
        'category':category,
        'brand':brands,
        'product':product,
        'banner':banner,
       }
    
    
    
    return render(request, 'shop.html',context)

def checkout(request):
    return render(request, 'checkout.html')

def login(request):
       
    if request.method == "POST" :
   
       username = request.POST.get('user')
       password = request.POST.get('password')
       user = authenticate (username=username, password=password)   
       if user is not None:
            auth_login(request, user)
            return redirect('/')
       elif user is None:
                return render(request, "login.html", {
                        "message": "Invalid username and/or password."
                })     
       
    return render(request, 'login.html')

def register(request):
    form = CreateUserForm()
    
    if request.method=='POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save() 
        
        
    context={
        'form':form,
    }
    return render(request, 'register.html',context)

def account(request):
    return render(request, 'account.html')

def wishlist(request):
    return render(request, 'wishlist.html')

def contact(request):
    return render(request, 'contact.html')

def cart(request):
    return render(request, 'cart.html')


def blogs(request):
    return render(request, 'blog.html')


def singleblog(request):
    return render(request, 'blog-single.html')
