from django.shortcuts import render, get_object_or_404
from .models import Product, Category


def home(request):
    products = Product.objects.filter(is_available=True)[:8]  # 8 последних товаров
    return render(request, 'flowers/home.html', {'products': products})


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(is_available=True)

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)

    return render(request, 'flowers/product_list.html', {
        'category': category,
        'categories': categories,
        'products': products,
    })


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'flowers/product_detail.html', {'product': product})
