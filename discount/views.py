from django.shortcuts import render, redirect
from .models import DiscountedItem
from cart.models import Cart, CartItem
from store.models import Product

def discounted_items(request):
    discounted_items = DiscountedItem.objects.all()
    return render(request, 'discount/discounted_items.html', {'discounted_items': discounted_items})

# def discounted_items(request):
#     discounted_items = DiscountedItem.objects.all()
#     for item in discounted_items:
#         item.discounted_price = item.product.price - (item.product.price * item.discount_percentage/100)
#     return render(request, 'discount/discounted_items.html', {'discounted_items': discounted_items})

# def _cart_id(request):
#     cart = request.session.session_key
#     if not cart:
#         cart = request.session.create()
#     return cart

# def update_discounted_price(cart_item):
#     # Calculate the discounted price and update the cart item
#     discounted_price = cart_item.product.price - (cart_item.product.price * cart_item.product.discount_percentage / 100)
#     cart_item.discounted_price = discounted_price
#     cart_item.save()

# def add_to_cart(request, product_id):
#     current_user = request.user
#     product = Product.objects.get(id=product_id) 
    
#     if current_user.is_authenticated:
#         is_cart_item_exists = CartItem.objects.filter(product=product, user=current_user).exists()
#         if is_cart_item_exists:
#             cart_items = CartItem.objects.filter(product=product, user=current_user)
#             item = cart_items.first()
#             item.quantity += 1
#             update_discounted_price(item)
#             item.save()
#         else:
#             try:
#                 cart = Cart.objects.get(cart_id=_cart_id(request)) 
#             except Cart.DoesNotExist:
#                 cart = Cart.objects.create(cart_id=_cart_id(request))
#             cart.save()
#             cart_item = CartItem.objects.create(
#                 product=product,
#                 quantity=1,
#                 cart=cart,
#                 user=current_user
#             )
#             update_discounted_price(cart_item)
#             cart_item.save()
#         return redirect('cart')
#     else:
#         try:
#             cart = Cart.objects.get(cart_id=_cart_id(request)) 
#         except Cart.DoesNotExist:
#             cart = Cart.objects.create(cart_id=_cart_id(request))
#             cart.save()
        
#         try:
#             cart_item = CartItem.objects.get(product=product, cart=cart)
#             cart_item.quantity += 1
#             update_discounted_price(cart_item)
#             cart_item.save()
#         except CartItem.DoesNotExist:
#             cart_item = CartItem.objects.create(
#                 product=product,
#                 quantity=1,
#                 cart=cart
#             )
#             update_discounted_price(cart_item)
#             cart_item.save()
#     return redirect('cart')