from django.contrib import admin
from .models import *
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

    def save_model(self, request, obj, form, change):
        if not obj.slug:
            obj.slug = slugify(obj.name)
        super().save_model(request, obj, form, change)
# Register your models here.
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)