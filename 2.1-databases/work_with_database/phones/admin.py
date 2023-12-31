from django.contrib import admin
from .models import Phone


@admin.register(Phone)
class PhoneAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'slug', 'image', 'release_date', 'lte_exists',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
