from django.urls import re_path

from .views import MainPageView

app_name = 'main'
urlpatterns = [
    re_path(r'^$', MainPageView.as_view(), name='main_page'),
]
