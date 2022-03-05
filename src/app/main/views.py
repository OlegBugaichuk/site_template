from django.views.generic import DetailView
from .models import MainPageDB


class MainPageView(DetailView):
    model = MainPageDB
    template_name = 'main/page.html'
    context_object_name = 'page'

    def get_object(self, queryset=None):
        return self.model.get_solo()