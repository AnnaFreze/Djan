from django.shortcuts import render, redirect
from phones.models import Phone
from phones.management.commands import import_phones

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    phones_all = Phone.objects.all()
    sorted_phones = request.GET.get('sort', '')

    if sorted_phones == 'max_price':
        phones = phones_all.order_by('-price').values()
        context = {'phones': phones}
        return render(request, template, context)

    elif sorted_phones == 'min_price':
        phones = phones_all.order_by('price').values()
        context = {'phones': phones}
        return render(request, template, context)

    elif sorted_phones == 'name':
        phones = phones_all.order_by('name').values()
        context = {'phones': phones}
        return render(request, template, context)

    context = {'phones': phones_all}
    return render(request, template, context)

def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug__contains=slug).first()
    context = {'phone': phone}
    return render(request, template, context)
