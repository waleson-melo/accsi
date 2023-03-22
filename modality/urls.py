from django.urls import path

from .views import ListModality


app_name = 'modality'

urlpatterns = [
    path('', ListModality.as_view(), name='list'),
]
