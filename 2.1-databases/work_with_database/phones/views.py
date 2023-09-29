from django.shortcuts import render, redirect

from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_type_get = request.GET.get('sort')

    if sort_type_get == 'min_price':
        sort_type = 'price'
    elif sort_type_get == 'max_price':
        sort_type = '-price'
    else:
        sort_type = 'name'

    phones_db = Phone.objects.all().order_by(sort_type)
    context = {'phones': phones_db}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    p1 = Phone.objects.get(slug=slug)
    context = {'phone': {'id': p1.id, 'name': p1.name, 'price': p1.price, 'image': p1.image, 'release_date': p1.release_date, 'lte_exists': p1.lte_exists, 'slug': p1.slug}}
    return render(request, template, context)
