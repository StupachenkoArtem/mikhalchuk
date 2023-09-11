from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *

menu = [{'title': 'Галерея', 'url_name': 'gallery'},
        {'title': 'Коллекции', 'url_name': 'collections'},
        {'title': "MIKHAL'CHUK", 'url_name': "MIKHAL'CHUK"},
        {'title': 'Контакты', 'url_name': 'contact'}]
menu2 = ["возврат и обмен товара", "доставка", "конфиденциальность", "публичная оферта"]


def index(request):
    posts = Clothes.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': "MIKHAL'CHUK"
    }

    return render(request, 'mikhalchuk/index.html', context=context)


def gallery(request):
    return render(request, 'mikhalchuk/gallery.html', {'title': 'GALLERY'})


def collections(request):
    return render(request, 'mikhalchuk/collections.html')


def mikhalchuk(request):
    return HttpResponse("MIKHAL'CHUK")


def contact(request):
    return render(request, 'mikhalchuk/contacts.html', {'title': 'MIKHALCHUK. Контакты'})


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Cтраница не найдена</h1>')


def show_post(request, post_id):
    return HttpResponse(f"Отображение поста с id = {post_id}")


def new_collection(request):
    return render(request, 'mikhalchuk/newcollection.html')


def dress(request):
    return render(request, 'mikhalchuk/dress.html')


def jackets(request):
    return render(request, 'mikhalchuk/jackets.html')


def shirts_and_blouses(request):
    return render(request, 'mikhalchuk/shirts_and_blouses.html')


def trousers_and_skirts(request):
    return render(request, 'mikhalchuk/trousers_and_skirts.html')
