from django.urls import path
from .views import markFavourtie, FavouriteProductListView


urlpatterns = [
    path('', FavouriteProductListView.as_view(), name='favourite-products'),
    path('mark/<int:id>/', markFavourtie, name='mark-favourite'),
]
 