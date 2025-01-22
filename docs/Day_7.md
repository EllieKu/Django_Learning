# Django Learning day 7

## Customize the admin form

[docs-admin site](https://docs.djangoproject.com/en/5.1/ref/contrib/admin/#django.contrib.admin.ModelAdmin)

`ModelAdmin` class 是 admin  interface 中的 model. 用來調整 UI 介面.

使用 `inlines` 關聯

Django 預設為使用 str() 展示 object. `list_display` 屬性將展示轉為 list of field name.

 `list_filter`  過濾器優化介面

`search_fields` 增加搜尋框

yl

polls/admin.py

```python
from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
  model = Choice
  extra = 3
 
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {"fields": ["question_text"]}),
    ("Date Information", {"fields": ["pub_date"]})
  ]
  inlines = [ChoiceInline]
  list_display = ["question_text", "pub_date", "was_published_recently"]
  list_filter = ["pub_date"]

```

使用 display() 裝飾該method

polls/models.py

```python
# ...
from django.contrib import admin

class Question(models.Model):
    # ...
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?"
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
```

## Reference

1. [https://docs.djangoproject.com/en/5.1/intro/tutorial07/](https://docs.djangoproject.com/en/5.1/intro/tutorial07/)
