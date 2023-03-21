from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import User


class CreateUser(CreateView):
    template_name = 'user/user_form.html'
    model = User
    fields = ['email', 'username', 'first_name', 'last_name', 'password']
    success_url = reverse_lazy('user:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Cadastrar Usuário'

        return context


class UpdateUser(UpdateView):
    template_name = 'user/user_form.html'
    model = User
    fields = ['email', 'username', 'first_name', 'last_name', 'password']
    success_url = reverse_lazy('user:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Alterar Usuário'

        return context


class ListUser(ListView):
    template_name = 'user/user_list.html'
    model = User
    context_object_name = 'users'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Usuários'

        return context
