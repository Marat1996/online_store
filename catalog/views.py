from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Cart


def home(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'catalog/home.html', context)

def contacts(request):
    return render(request, 'catalog/contact.html')

def product_detail(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'catalog/product_detail.html', context)


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