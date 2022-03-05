from django.contrib import admin
from solo.admin import SingletonModelAdmin

from .models import MainPageDB


@admin.register(MainPageDB)
class MainPageAdmin(SingletonModelAdmin):
    pass
