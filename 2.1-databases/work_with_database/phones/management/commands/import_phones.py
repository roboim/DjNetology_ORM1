import csv

from django.core.management.base import BaseCommand
from django.template.defaultfilters import slugify
from phones.models import Phone


class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for phone in phones:
            # Сохранение модели
            p = Phone.objects.filter(name=phone['name']).exists()
            if p is False:
                slug_get = slugify(phone['name'])
                Phone.objects.create(pk=phone['id'], name=phone['name'], price=phone['price'], image=phone['image'],
                                     release_date=phone['release_date'], lte_exists=phone['lte_exists'], slug=slug_get)
                print(f"Добавлен новый продукт {phone['name']}")
            else:
                print(f"Продукт уже существует {phone['name']}")