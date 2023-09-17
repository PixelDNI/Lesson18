from django.db import models
# Create your models here.
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=70)

    def __str__(self):
        return self.name


class Product(models.Model):
    STATUS = (
        ('O', 'on_storage'),
        ('P', 'is_packing'),
        ('D', 'is_delivering'),
        ('R', 'received')
    )

    name = models.CharField(max_length=70)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    status_of_purchasing = models.CharField(choices=STATUS, max_length=70, default='O')
    date_of_purchasing = models.DateField(null=True)
    slug = models.SlugField(max_length=255, unique=True, null=True)

    def __str__(self):
        return f"{self.name} - {self.category} - {self.price} - {self.status_of_purchasing}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super(Product, self).save(*args, **kwargs)

    def show_status(self):
        for i in self.STATUS:
            if self.status_of_purchasing == i[0]:
                return i[1]

