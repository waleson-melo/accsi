from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .models import Student


class CreateStudent(CreateView):
    template_name = 'student/student_form.html'
    model = Student
    fields = ['registration', 'name', 'email', 'phone_number']
    success_url = reverse_lazy('student:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Alunos'

        return context


class UpdateStudent(UpdateView):
    template_name = 'student/student_form.html'
    model = Student
    fields = ['registration', 'name', 'email', 'phone_number']
    success_url = reverse_lazy('student:list')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = 'Alunos'

        return context

class ListStudents(ListView):
    template_name = 'student/student_list.html'
    model = Student
    context_object_name = 'students'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, object_list=None, **kwargs)
        context['page_title'] = 'Alunos'

        return context
