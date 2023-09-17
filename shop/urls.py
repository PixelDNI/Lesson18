from django.urls import path
from .views import *
urlpatterns = [
    path('update_product/<str:slug>/', UpdateProduct.as_view(), name='update_product'),
    path('add_new_product/', AddProduct.as_view(), name='add_new_product'),
    path('', ShowProductsView.as_view(), name='show_products'),
    path('delete_product/<str:slug>/', DeleteProduct.as_view(), name='delete_product'),
]
