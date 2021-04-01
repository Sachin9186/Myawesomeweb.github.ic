from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="ShopHome"),
    path('about/', views.about, name="AboutUs"),
    path('contact/', views.contact, name="ContactUs"),
    path('products/<int:myid>', views.ProductView, name="ProductView"),
    path('checkout/', views.checkout, name="CheckOut"),
    path('handlerequest/', views.handlerequest, name="HandleRequest"),

]