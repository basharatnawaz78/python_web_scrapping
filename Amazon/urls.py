from django.contrib import admin
from django.urls import path
from Amazon import views 
urlpatterns = [
    path("", views.index, name='home'),
    path("product", views.product, name='product'),
    path("AmazonList", views.AmazonList, name='AmazonList'),
    path("FlipkartList", views.FlipkartList, name='FlipkartList'),
    path('pdfreport',views.pdfreport)
   
]
