from django.views.generic.list import ListView

from .models import Modality


class ListModality(ListView):
    template_name = 'modality/modality_list.html'
    model = Modality
    context_object_name = 'modalities'

    def get_context_data(self, *args, object_list=None, **kwargs):
        context = super().get_context_data(*args, object_list=None, **kwargs)
        context['page_title'] = 'Modalidades'

        return context
