from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart, Category


def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'catalog/home.html', context)

def contacts(request):
    return render(request, 'catalog/contacts.html')


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {
        'product': product,
    }
    return render(request, 'catalog/product_detail.html', context)


def cart(request):
    return render(request, 'catalog/cart.html')
@login_required
def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)

        # Добавляем продукт в корзину
        cart_item, created = Cart.objects.get_or_create(
            user=request.user,
            product=product,
            defaults={'quantity': 1}
        )

        if not created:
            cart_item.quantity += 1
            cart_item.save()

        # Перенаправляем пользователя на страницу корзины или на главную страницу
        return redirect('cart')
    else:
        return redirect('home')


def category_products(request, slug):
    category = Category.objects.get(slug=slug)
    products = Product.objects.filter(category=category)
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'catalog/category_products.html', context)