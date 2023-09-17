from django.urls import path, include
from .views import *
urlpatterns = [
    path('', StartCustomerPage.as_view(), name='start_customer_page'),
    path('show_product/<str:slug>/', ShowProduct.as_view(), name='show_product')

]