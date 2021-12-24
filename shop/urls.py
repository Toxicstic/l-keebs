from django.urls import path
from . import views

urlpatterns = [
    path('', views.shop, name='shop-shop'),
    path('listing/', views.shop, name='shop-listing'),
]
