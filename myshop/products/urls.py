from django.urls import path
from .views import product_list

urlpatterns = [
    path('shop/', product_list, name='product_list'),
]
