from django.db import models
from mixin import DateMixin
from products.models import Product
from users.models import User

# Create your models here.

class FavouriteProduct(DateMixin):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user')
    is_favourite = models.BooleanField(default=True)

    def __str__(self):
        return 'product {} {} by {}'.format(self.product.name, 'marked favourite', self.user.get_full_name())