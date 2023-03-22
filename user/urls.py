from django.urls import path

from .views import CreateUser, UpdateUser, ListUser


app_name = 'user'

urlpatterns = [
    path('cadastrar/<int:meu>/', CreateUser.as_view(), name='create'),
    path('alterar/<int:pk>/', UpdateUser.as_view(), name='update'),
    path('usuarios/', ListUser.as_view(), name='list'),
]
