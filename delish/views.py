from django.shortcuts import render, get_object_or_404, redirect
from store.models import Product
from category.models import Category
from django.core.paginator import Paginator

def home(request, category_slug=None):

    if category_slug : 
        category = get_object_or_404(Category, slug = category_slug)
        products = Product.objects.filter(is_available = True, category=category) 
        page = request.GET.get('page')
        print(page)
        paginator = Paginator(products, 3) 
        paged_product = paginator.get_page(page)
    else : 
        products = Product.objects.filter(is_available = True) 
        paginator = Paginator(products, 3) 
        page = request.GET.get('page')
        paged_product = paginator.get_page(page)
        
        
    categories = Category.objects.all()
    context = {'products' : paged_product, 'categories' : categories, }
    return render(request, 'index.html', context)
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')