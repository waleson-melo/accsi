from django.urls import path

from .views import ListStudents, CreateStudent, UpdateStudent


app_name = 'student'

urlpatterns = [
    path('', ListStudents.as_view(), name='list'),
    path('cadastrar/', CreateStudent.as_view(), name='create'),
    path('alterar/<int:pk>', UpdateStudent.as_view(), name='update'),
]
