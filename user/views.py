from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import User


class CreateUser(CreateView):
    template_name = 'user/user_form.html'
    model = User
    fields = ['email', 'username', 'first_name', 'last_name', 'password']
    success_url = reverse_lazy('user:list')

    def dispatch(self, request, *args, **kwargs):
        self.aluno = kwargs.get('meu', None)
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Cadastrar' + str(self.aluno)

        return context

    def form_valid(self, form):
        # form.instance.email = 'haro'
        return super().form_valid(form)


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

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=2)
        return queryset
