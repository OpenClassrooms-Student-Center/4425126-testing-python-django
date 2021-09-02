from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView

from .models import FavouriteProduct
from products.models import Product
from get_user import get_user


@method_decorator(login_required, name='dispatch')
class FavouriteProductListView(ListView):
    '''
    List the favourite product of an user
    '''
    template_name = 'favourite_product.html'
    model = FavouriteProduct

    def get_queryset(self):
        return self.model.objects.filter(user = get_user().id, is_favourite=True)

    def get(self, request):
        return super().get(request)


@csrf_exempt
def markFavourtie(request, id):
    '''
    Marks or unmark the product as favourite.

    Parameters:
        id (int): An id of product
    Returns:
        json response of success or failure 
    '''
    if request.method == 'AJAX':
        product = Product.objects.get(id=id)
        if not Product:
            JsonResponse({'success': False})
        favourite_obj, created = FavouriteProduct.objects.get_or_create(product=product, user=request.user)
        if not created:
            favourite_obj = FavouriteProduct.objects.get(id = favourite_obj.id)
            if favourite_obj.is_favourite:
                favourite_obj.is_favourite = False
            else:
                favourite_obj.is_favourite = True
            favourite_obj.save(update_fields=['is_favourite'])
        return JsonResponse({'success': True, 'marked': favourite_obj.is_favourite})
    JsonResponse({'success': False})