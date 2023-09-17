from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView
# Create your views here.
from shop.forms import *
from .models import Product
from .forms import AddNewProductForm


class AddProduct(TemplateView):
    template_name = 'shop/add_product.html'

    def get(self, request):
        form = AddNewProductForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = AddNewProductForm(request.POST)
        if form.is_valid():
            # Save the form data to the database or perform other actions
            form.save()
            return redirect('show_products')  # Redirect to a success page
        else:
            return render(request, self.template_name, {'form': form})


class ShowAllProductsViews(ListView):
    template_name = 'clientSide/start_page.html'
    model = Product


class UpdateProduct(UpdateView):
    template_name = 'shop/update_product.html'
    model = Product  # Specify the model
    form_class = UpdateProductForm  # Specify the form class

    success_url = '/admin_side/'


class ShowProductsView(ListView):
    template_name = 'shop/show_all_products.html'
    model = Product


class DeleteProduct(DeleteView):
    template_name = 'shop/delete_product.html'
    model = Product
    success_url = '/admin_side/'


    # def delete(self, request, *args, **kwargs):
    #     self.object = self.get_object()
    #     # Perform any additional logic before deleting the object
    #     self.object.delete()
    #     return super().delete(request, *args, **kwargs)
