from django.urls import reverse, resolve
from favourites.views import markFavourtie, FavouriteProductListView

class TestFavouritesUrls:
    def test_favourite_products(self):

        """
        Testing if the 'favourite-products' route is mapping to FavouriteProductListView
        """

        url = reverse('favourite-products')
        assert resolve(url).view_name == 'favourite-products'
        assert resolve(url).func.view_class == FavouriteProductListView


    def test_mark_favourite(self):

        """
        Testing if the 'mark-favourite' route is mapping to markFourite view
        """

        url = reverse('mark-favourite', args=[1])
        assert resolve(url).view_name == 'mark-favourite'
        assert resolve(url).func == markFavourtie