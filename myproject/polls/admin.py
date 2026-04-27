from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import Question, Choice


class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3
  

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {"fields": ["question_text"]}),
    (_("Date Information"), {"fields": ["pub_date"]})
  ]
  inlines = [ChoiceInline]
  list_display = ["question_text", "pub_date", "was_published_recently"]
  list_filter = ["pub_date"]
  search_fields = ["question_text"]
