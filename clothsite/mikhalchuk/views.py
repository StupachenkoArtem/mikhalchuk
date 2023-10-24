from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView
from .forms import LoginUserForm
from .models import *
from .utils import DataMixin

menu = [{'title': 'Галерея', 'url_name': 'gallery'},
        {'title': 'Коллекции', 'url_name': 'collections'},
        {'title': "MIKHAL'CHUK", 'url_name': "MIKHAL'CHUK"},
        {'title': 'Контакты', 'url_name': 'contact'}]


class RegisterUser(DataMixin, CreateView):
    form_class = UserCreationForm
    template_name = 'mikhalchuk/register.html'
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return {**context, **c_def}


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'mikhalchuk/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return {**context, **c_def}

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def index(request):
    context = {
        'menu': menu,
        'title': "MIKHAL'CHUK"
    }

    return render(request, 'mikhalchuk/index.html', context=context)


def gallery(request):
    return render(request, 'mikhalchuk/gallery.html', {'title': 'GALLERY'})


def collections(request):
    collections = Collections.objects.all()
    context = {
        'menu': menu,
        'title': "COLLECTIONS",
        'collections': collections
    }
    return render(request, 'mikhalchuk/collections.html', context=context)


# class CollectionImageView(DetailView):
#     model = Collections
#     template_name = 'mikhalchuk/collection_image.html'
#     context_object_name = 'collection'
#
#     def get_object(self, queryset=None):
#         return get_object_or_404(Collections, slug=self.kwargs['coll_slug'])


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


def favicon_ico(request):
    return HttpResponse("favicon.ico")
