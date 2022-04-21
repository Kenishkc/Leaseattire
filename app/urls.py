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
    path('cart', views.cart,name='cart'),
    path('contact', views.contact),
    path('blogs', views.blogs),
    path('blog-single', views.singleblog),
    path('user-profile/<str:id>',views.profile),
    path('edit-profile/<str:id>',views.profileSetting),
    
    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),

]