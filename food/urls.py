from django.urls import path
from . import views as food_views

urlpatterns = [
    path('', food_views.home, name='food-home'),
    path('about/', food_views.about, name='food-about'),
    path('menu/', food_views.MenuView.as_view(), name='food-menu'),
    path('cart/', food_views.cart, name='food-cart'),
]
