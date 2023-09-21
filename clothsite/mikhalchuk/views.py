from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *

menu = [{'title': 'Галерея', 'url_name': 'gallery'},
        {'title': 'Коллекции', 'url_name': 'collections'},
        {'title': "MIKHAL'CHUK", 'url_name': "MIKHAL'CHUK"},
        {'title': 'Контакты', 'url_name': 'contact'}]
menu2 = ["возврат и обмен товара", "доставка", "конфиденциальность", "публичная оферта"]


def index(request):
    context = {
        'menu': menu,
        'title': "MIKHAL'CHUK"
    }

    return render(request, 'mikhalchuk/index.html', context=context)


def gallery(request):
    return render(request, 'mikhalchuk/gallery.html', {'title': 'GALLERY'})


def collections(request):
    context = {
        'menu': menu,
        'title': "COLLECTIONS"
    }
    collections = Collections.objects.all()
    return render(request, 'mikhalchuk/collections.html', context=context)


def mikhalchuk(request):
    return HttpResponse("MIKHAL'CHUK")


def contact(request):
    context = {
        'menu': menu,
        'title': "MIKHALCHUK. Контакты"
    }
    return render(request, 'mikhalchuk/contacts.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Cтраница не найдена</h1>')


def show_post(request, post_id):
    return HttpResponse(f"Отображение поста с id = {post_id}")


def new_collection(request):
    context = {
        'menu': menu,
        'title': "NEW_COLLECTION"
    }
    return render(request, 'mikhalchuk/newcollection.html', context=context)


def dress(request):
    context = {
        'menu': menu,
        'title': "DRESS"
    }
    return render(request, 'mikhalchuk/dress.html', context=context)


def jackets(request):
    context = {
        'menu': menu,
        'title': "JACKETS"
    }
    return render(request, 'mikhalchuk/jackets.html', context=context)


def shirts_and_blouses(request):
    context = {
        'menu': menu,
        'title': "SHIRTS_AND_BLOUSES"
    }
    return render(request, 'mikhalchuk/shirts_and_blouses.html', context=context)


def trousers_and_skirts(request):
    context = {
        'menu': menu,
        'title': "TROUSERS_AND_SKIRTS"
    }
    return render(request, 'mikhalchuk/trousers_and_skirts.html', context=context)
