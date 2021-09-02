from django.shortcuts import redirect
from django.views.generic import ListView

from products.models import Product


def RedirectHomeView(request):
    '''
    Redirect url from '/' to '/home/'
    '''
    return redirect('home')

class HomeView(ListView):
    '''
    Renders home page with all the products
    '''
    template_name = 'home.html'
    model = Product

    def get(self, request):
        return super().get(request)
