from django.contrib import admin
from django.urls import path
from Amazon import views 
urlpatterns = [
    path("", views.index, name='home'),
    path("product", views.product, name='product')
]
