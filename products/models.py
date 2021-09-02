from django.db import models

from mixin import DateMixin
from get_user import get_user


class Product(DateMixin):
    name = models.CharField(max_length=20, null=False, blank=False)
    image = models.ImageField(upload_to='product_img/', null=False)
    description = models.CharField(max_length=100, null=False, blank=False)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

    def is_favourite(self):
        t = Product.objects.distinct().filter(product__user=get_user().id,
                                              product__product=self.id, product__is_favourite=True).first()
        return True if t else False
