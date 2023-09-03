from django.urls import path
from . import views


urlpatterns = [
   path('', views.discounted_items, name='discounted_items'),
#    path('cart/<int:product_id>/', views.add_to_cart, name='add_cart'),
]
