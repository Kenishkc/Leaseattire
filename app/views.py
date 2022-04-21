
from django.shortcuts import render ,redirect
from app.models import  Category,Brand,Product,Banner,Sub_Category,Profile
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login as auth_login
from django.contrib import messages 
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from cart.cart import Cart






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
    brands=Brand.objects.all()
    category= Category.objects.all()
    product =Product.objects.filter(id=id).first()
    
    context={
        'brand':brands,
        'product':product,
        'category':category,
      
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
            messages.success(request, "Login successfully!")
            return redirect('/')
       elif user is None:
                messages.error(request, "Please Enter valid username or password!")    
       
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

def logoutUser(request):
     logout(request)
     messages.success(request, "Your logout, Get back Soon !")
     return redirect("/")
  
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


def profile(request,id):
    user =User.objects.filter(id=id).first()
    profile =Profile.objects.filter(user=user).first()
    if profile :  
      context={
        'profile':profile,
        }
      return render(request, 'user/profile.html',context)
    else:
     return render(request, 'user/add.html')
 
def storeUserProfile(request):
    user =User.objects.filter(id=request.user.id).first()
    if request.method=='POST':
         first = request.POST.get('fullname')
         nick = request.POST.get('nickname')
         mobile_one = request.POST.get('mobile_one')
         mobile_two = request.POST.get('mobile_two')
         district = request.POST.get('district')
         city = request.POST.get('city')
         local_area = request.POST.get('local_area')
         street_address = request.POST.get('street_address')
         house_number = request.POST.get('house_number')
         birthday = request.POST.get('birthday')
         gender = request.POST.get('gender')
         image = request.POST.get('image')
    data=Profile(user=user,fullname=first,nickname=nick,phone_number=mobile_one,second_number=mobile_two,
                 disctrict=district,city=city,local_area=local_area,
                 house_number=house_number,birthday=birthday,gender=gender,profile_picture=image)
    data.save()
    messages.success(request, "Your Profile has Sucessfully saved!")
    return redirect("/")
 
def profileSetting(request,id):
    profile =Profile.objects.filter(user=id).first()
    context={
        'profile':profile,
        }
    
    return render(request, 'user/edit.html',context)
    
    

@login_required(login_url="/user-login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    messages.success(request, "Product added to cart !")
    return redirect("/")


@login_required(login_url="/user-login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart")


@login_required(login_url="/user-login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart")


@login_required(login_url="/user-login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart")


@login_required(login_url="/user-login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart")


@login_required(login_url="/user-login")
def cart_detail(request):
    return render(request, 'cart/cart_detail.html')