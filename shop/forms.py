from django.forms import forms, ModelForm, DateInput
from django.utils.text import slugify

from .models import Product


class AddNewProductForm(ModelForm):

    class Meta:
        model = Product
        exclude = ('slug',)

    widgets = {
        'date_of_purchasing': DateInput(attrs={'type': 'date'}),
    }

class UpdateProductForm(ModelForm):

    class Meta:
        model = Product
        exclude = ('slug',)

    widgets = {
        'date_of_purchasing': DateInput(attrs={'type': 'date'}),
    }

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name')  # Assuming 'name' is the field used to generate the slug
        if name:
            slug = slugify(name)
            cleaned_data['slug'] = slug
        return cleaned_data
