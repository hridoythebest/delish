from django.shortcuts import render, redirect
from .forms import RegistrationForm, EditProfileForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required



from cart.models import Cart, CartItem
def get_create_session(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key
def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('cart')
    return render(request, 'accounts/register.html', {'form':form})

def profile(request):
    return render(request, 'accounts/dashboard.html')

def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=user_name, password=password)
        
        if user is not None:
            login(request, user)
            session_key = get_create_session(request)

            try:
                cart = Cart.objects.get(cart_id=session_key)
            except Cart.DoesNotExist:
                cart = Cart.objects.create(cart_id=session_key)

            cart_items = CartItem.objects.filter(cart=cart)
            for item in cart_items:
                item.user = user
                item.save()

            return redirect('profile')
    
    return render(request, 'accounts/signin.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'accounts/edit_profile.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')