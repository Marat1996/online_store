from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView, View, ListView, CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404, redirect
from .models import Product, Cart, Category

# Home Page
class HomeView(TemplateView):
    template_name = 'catalog/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['products'] = Product.objects.all()
        return context

# Product List Page
class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

# Product Detail Page
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
    context_object_name = 'product'

# Contacts Page
class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'

# Cart Page
class CartView(TemplateView):
    template_name = 'catalog/cart.html'

# Add to Cart
class AddToCartView(LoginRequiredMixin, View):
    def post(self, request):
        product_id = request.POST.get('product_id')
        product = get_object_or_404(Product, id=product_id)

        # Add product to cart
        cart_item, created = Cart.objects.get_or_create(
            user=request.user,
            product=product,
            defaults={'quantity': 1}
        )

        if not created:
            cart_item.quantity += 1
            cart_item.save()

        # Redirect to cart page or home page
        return redirect('cart')

# Category Products Page
class CategoryProductsView(TemplateView):
    template_name = 'catalog/category_products.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        slug = self.kwargs['slug']
        category = get_object_or_404(Category, slug=slug)
        context['category'] = category
        context['products'] = Product.objects.filter(category=category)
        return context