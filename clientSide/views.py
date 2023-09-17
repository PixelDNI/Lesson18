from django.views.generic import *
from shop.models import Product
from django.shortcuts import get_object_or_404, redirect


class StartCustomerPage(ListView):
    template_name = 'clientSide/start_page.html'
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(status_of_purchasing='O')

class ShowProduct(UpdateView):
    template_name = 'clientSide/show_product.html'

    model = Product
    fields = []

    def form_valid(self, form):
        product = form.save(commit=False)
        product.status_of_purchasing = 'P'  # Change the status to 'is_packing'
        product.save()
        return redirect('start_customer_page')




