from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from players.utils import *

from players.models import *
from players.forms import *




class PlayersHome(DataMixin, ListView):
    model = Player
    template_name = 'players/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['menu'] = menu
        # context['title'] = 'Home page'
        # context['cat_selected'] = 0
        # context['cats'] = Category.objects.all()
        c_def = self.get_user_context(title='Home page')
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Player.objects.filter(is_published=True)




# def index(request):
#     posts = Player.objects.all()
#     cats = Category.objects.all()
#     context= {
#         'menu': menu,
#         'posts':posts,
#         'cats': cats,
#         'cat_selected': 0,
#     }
#
#     return render(request, 'players/index.html', context=context)

class PlayersCategory(DataMixin, ListView):
    model = Category
    template_name = 'players/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Player.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Category - ' + str(context['posts'][0].cat), cat_selected=context['posts'][0].cat_id)
        # context['menu'] = menu
        # context['title'] = 'Category - ' + str(context['posts'][0].cat)
        # context['cat_selected'] = context['posts'][0].cat_id
        # context['cats'] = Category.objects.all()
        # print(context['posts'][0])
        return dict(list(context.items()) + list(c_def.items()))

# def show_category(request, cat_id):
#     posts = Player.objects.filter(cat_id=cat_id)
#     cats = Category.objects.all()
#     context= {
#         'menu': menu,
#         'posts':posts,
#         'cats': cats,
#         'title': 'Show category',
#         'cat_selected': cat_id,
#     }
#
#     return render(request, 'players/index.html', context=context)


class PlayerShowPost(DataMixin, DetailView):
    model = Player
    template_name = 'players/post.html'
    context_object_name = 'posts'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title=context['posts'])
        # context['menu'] = menu
        # context['title'] = context['posts']
        # context['cats'] = Category.objects.all()
        # context['cat_selected'] = context['post'][0].cat_id
        return dict(list(context.items()) + list(c_def.items()))

# def show_post(request, post_id):
#     posts = get_object_or_404(Player, pk=post_id)
#     cats = Category.objects.all()
#     context= {
#         'menu': menu,
#         'posts':posts,
#         'cats': cats,
#         'title': posts.title,
#         'cat_selected': posts.cat_id,
#     }
#
#     return render(request, 'players/post.html', context=context)


def about(request):
    return HttpResponse("this is about")



class UserLogin(DataMixin, LoginView):
    form_class = PlayersLoginForm
    template_name = 'players/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)
        c_raul = self.get_user_context(title='Authentication')
        return dict(list(context.items()) + list(c_raul.items()))

    def get_success_url(self):
        return reverse_lazy('home')


class RegisterUser(DataMixin, CreateView):
    form_class = PlayersResitrationForm
    template_name = 'players/register.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_raul = self.get_user_context(title='User registration')
        return dict(list(context.items()) + list(c_raul.items()))

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')


def feedback(request):
    return HttpResponse("this is feedback")


class PlayerAddPost(DataMixin, CreateView):
    form_class = AddPostFrom
    template_name = 'players/add_post.html'
    # context_object_name = 'posts'
    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_raul = self.get_user_context(title='Adding post')
        # context['menu'] = menu
        # context['title'] = 'Adding post'
        return dict(list(context.items()) + list(c_raul.items()))

# def add_post(request):
#
#     cats = Category.objects.all()
#     if request.method == 'POST':
#         form = AddPostFrom(request.POST, request.FILES )
#         if form.is_valid():
#             # print(form.cleaned_data)
#             try:
#                 # Player.objects.create(**form.cleaned_data)
#                 form.save()
#                 return redirect('home')
#             except:
#                 form.add_error(None, "Error of adding post")
#     else:
#         form = AddPostFrom()
#     context = {
#         'menu': menu,
#         'cats': cats,
#         'title': "Adding post",
#         'form': form,
#     }
#     return render(request, 'players/add_post.html', context=context)
#
#

