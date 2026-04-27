from re import VERBOSE
import datetime
from django.contrib import admin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

class Question(models.Model):
    question_text = models.CharField(max_length=200, verbose_name=_('question_text'))
    pub_date = models.DateTimeField(verbose_name=_('pub_date'))

    @admin.display(
        boolean=True,
        ordering="pub_date",
        description=_("is_published_recently")
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    class Meta:
        verbose_name = _('question')
        verbose_name_plural = _('question')

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200, verbose_name=_('choice_text'))
    votes = models.IntegerField(default=0, verbose_name=_('votes'))

    class Meta:
        verbose_name = _('choice')
        verbose_name_plural = _('choice')