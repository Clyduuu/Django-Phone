from django.core.management.base import BaseCommand
from Phones.models import Manufacturer, Phone, Accessory

class Command(BaseCommand):
    help = 'Create initial data for the application'

    def handle(self, *args, **options):
        manufacturers = [
            {"name": "Manufacturer 1"},
            {"name": "Manufacturer 2"},
        ]

        phones = [
            {
                "name": "Phone 1",
                "manufacturer_name": "Manufacturer 1",
                "price": 500.00,
                "release_date": "2020-01-01",
            },
            {
                "name": "Phone 2",
                "manufacturer_name": "Manufacturer 2",
                "price": 600.00,
                "release_date": "2020-02-01",
            },
            # Add Airpods and TV
            {
                "name": "Airpods",
                "manufacturer_name": "Manufacturer 1",
                "price": 150.00,
                "release_date": "2020-04-01",
            },
            {
                "name": "TV",
                "manufacturer_name": "Manufacturer 2",
                "price": 1000.00,
                "release_date": "2020-05-01",
            },
        ]

        accessories = [
            {
                "name": "Accessory 1",
                "phone_name": "Phone 1",
                "price": 20.00,
            },
            {
                "name": "Accessory 2",
                "phone_name": "Phone 2",
                "price": 25.00,
            },
            # Add accessories for Airpods and TV
            {
                "name": "Airpods Case",
                "phone_name": "Airpods",
                "price": 10.00,
            },
            {
                "name": "TV Stand",
                "phone_name": "TV",
                "price": 50.00,
            },
        ]

        for manufacturer_data in manufacturers:
            _, created = Manufacturer.objects.get_or_create(**manufacturer_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Manufacturer '{manufacturer_data['name']}' created"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Manufacturer '{manufacturer_data['name']}' already exists"))

        for phone_data in phones:
            manufacturer_name = phone_data.pop("manufacturer_name")
            manufacturer = Manufacturer.objects.get(name=manufacturer_name)
            phone_data["manufacturer"] = manufacturer
            _, created = Phone.objects.get_or_create(**phone_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Phone '{phone_data['name']}' created"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Phone '{phone_data['name']}' already exists"))

        for accessory_data in accessories:
            phone_name = accessory_data.pop("phone_name")
            phone = Phone.objects.get(name=phone_name)
            accessory_data["phone"] = phone
            _, created = Accessory.objects.get_or_create(**accessory_data)
            if created:
                self.stdout.write(self.style.SUCCESS(f"Accessory '{accessory_data['name']}' created"))
            else:
                self.stdout.write(self.style.SUCCESS(f"Accessory '{accessory_data['name']}' already exists"))

        self.stdout.write(self.style.SUCCESS("Initial data created successfully"))
