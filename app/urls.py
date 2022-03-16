from django.urls import path
from . import views

urlpatterns = [
    path('', views.master),  #the path for our index view
    path('shop', views.shop),
    path('product-details', views.productDetails),
    path('checkout', views.checkout),
    path('user-login', views.login),
    path('user-register', views.register),
    path('account', views.account),
    path('wishlist', views.wishlist),
    path('cart', views.cart),
    path('contact', views.contact),
    path('blogs', views.blogs),
    path('blog-single', views.singleblog),
]