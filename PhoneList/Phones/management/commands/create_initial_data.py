from django.core.management.base import BaseCommand
from django.utils import timezone
from Phones.models import Brand, Category, Product, Customer, Order, OrderItem
import random

class Command(BaseCommand):
    help = 'Populate initial data for the gadget store website'

    def handle(self, *args, **options):
        # Create Brands
        brand_names = ['Samsung', 'Apple', 'Sony', 'LG', 'Dell']
        brands = [Brand.objects.create(name=name) for name in brand_names]

        # Create Categories
        category_names = ['Smartphones', 'Laptops', 'TVs', 'Headphones', 'Cameras']
        categories = [Category.objects.create(name=name) for name in category_names]

        # Create Products
        for i in range(10):
            product = Product.objects.create(
                name=f'Product{i + 1}',
                description=f'Description for Product{i + 1}',
                price=random.uniform(100.0, 2000.0),
                brand=brands[i % len(brands)],
            )
            product.category.set(random.sample(categories, random.randint(1, len(categories))))

        # Create Customers
        customer_names = ['John Doe', 'Jane Smith', 'Bob Johnson', 'Alice Brown', 'Chris Davis']
        customers = [Customer.objects.create(name=name, email=f'{name.lower().replace(" ", "_")}@example.com', phone_number='1234567890') for name in customer_names]

        # Create Orders
        for i in range(5):
            order = Order.objects.create(
                order_date=timezone.now(),
                total_amount=random.uniform(100.0, 1000.0),
                customer=customers[i % len(customers)],
            )

            # Create OrderItems
            for j in range(2):
                product = random.choice(Product.objects.all())
                order_item = OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=random.randint(1, 5),
                )

        self.stdout.write(self.style.SUCCESS('Successfully populated initial data'))