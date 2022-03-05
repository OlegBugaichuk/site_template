from django.db import models
from django.utils.translation import gettext_lazy as _
from solo.models import SingletonModel


class MainPageDB(SingletonModel):
    title = models.CharField(_('Title'), max_length=20)

    class Meta:
        verbose_name = _('Main page')
        verbose_name_plural = _("Main page")

    def __str__(self):
        return 'Main page'
