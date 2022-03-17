from django.shortcuts import render
from app.models import  Category,Brand,Product,Banner,Sub_Category

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
    
    subcategoryId=request.GET.get('sub_cat')
    if subcategoryId:
         product =Product.objects.filter(sub_category==subcategoryId)
    
        
    context={
        'category':category,
        'brand':brands,
        'product':product,
        'banner':banner,
        'subcategory':subcategory
    }
    return render(request, 'index.html',context)

def productDetails(request, id):
    product =Product.objects.filter(id=id).first()
    context={
        
        'product':product,
      
    }
    
    return render(request, 'productDetails.html',context)

def shop(request):
    return render(request, 'shop.html')

def checkout(request):
    return render(request, 'checkout.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

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
