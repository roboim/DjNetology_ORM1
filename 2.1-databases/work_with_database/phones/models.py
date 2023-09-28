from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=255, unique=True, verbose_name='Название')
    price = models.FloatField(blank=False, verbose_name='Цена')
    image = models.URLField(max_length=200, blank=False, verbose_name='Ссылка на фото')
    release_date = models.DateField(blank=False, verbose_name='Дата начала продаж')
    lte_exists = models.BooleanField(default=False, verbose_name='Функция LTE')
    slug = models.SlugField(verbose_name='Slug')

    def __str__(self):
        return f'{self.name}'
