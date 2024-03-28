import json
from django.core.management.base import BaseCommand
from catalog.models import Category, Product

class Command(BaseCommand):
    help = 'Заполнение БД из фикстур'

    def handle(self, *args, **options):
        self.stdout.write('Удаление старых данных')
        models = [Category, Product]
        for model in models:
            model.objects.all().delete()

        self.stdout.write('Запись новых данных')
        categories = self.load_data('fixtures/categories.json')
        self.seed_categories(categories)

        products = self.load_data('fixtures/products.json')
        self.seed_products(products)

        self.stdout.write(self.style.SUCCESS('БД заполнена'))

    def load_data(self, fixture_file):
        with open(fixture_file, 'r') as f:
            data = json.load(f)
        return data

    def seed_categories(self, categories):
        for category_data in categories:
            category = Category(**category_data['fields'])
            category.save()

    def seed_products(self, products):
        for product_data in products:
            category_name = product_data['fields']['category']
            category = Category.objects.get(name=category_name)
            product = Product(category=category, **product_data['fields'])
            product.save()