from django.urls import path
from . import views

urlpatterns = [
    path('', views.master),  #the path for our index view
    path('shop', views.shop),
    path('product-details/<str:id>', views.productDetails),
    path('checkout', views.checkout),
    path('user-login', views.login),
    path('user-register', views.register),
    path('user-logout', views.logoutUser),
    path('account', views.account),
    path('store-profile', views.storeUserProfile,name='storeprofile'),
    path('wishlist', views.wishlist),
    path('cart', views.cart),
    path('contact', views.contact),
    path('blogs', views.blogs),
    path('blog-single', views.singleblog),
    path('user-profile/<str:id>',views.profile),
]