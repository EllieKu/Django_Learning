# Django Learning day 4

## Creating Form

- 創建一個 HTML  `<form>` , method=”post”
- `forloop.counter`  表示 for 迴圈了幾次
- 為防範 CSRF 所有對內部 URL 的 POST 表單都該使用 [**`{% csrf_token %}`**](https://docs.djangoproject.com/zh-hans/5.1/ref/templates/builtins/#std-templatetag-csrf_token)

polls/templates/polls/detail.html

```html
<form action="{% url 'polls:vote' question.id %}" method="post">
{% csrf_token %}
<fieldset>
    <legend><h1>{{ question.question_text }}</h1></legend>
    {% if error_message %}<p><strong>{{ error_message }}</strong></p>{% endif %}
    {% for choice in question.choice_set.all %}
        <input type="radio" name="choice" id="choice{{ forloop.counter }}" value="{{ choice.id }}">
        <label for="choice{{ forloop.counter }}">{{ choice.choice_text }}</label><br>
    {% endfor %}
</fieldset>
<input type="submit" value="Vote">
</form>
```

polls/urls.py

```python
path("<int:question_id>/vote/", views.vote, name="vote"),
```

polls.views.py

```python
from django.db.models import F
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse

from .models import Choice, Question

# ...
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()

        return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))
```

- `request.POST`  is a dictionary-like object.  使用 `request.POST[’choice’]`  獲取值
- `F(”votes”) + 1` 指示數據庫將 votes 加 1
- 總是返回 `HttpResponseRedirect`
- `reverse()` 避免用硬編碼路徑, 給定要跳轉的 name of view and variable

## Use generic views

通用視圖將常見模式抽象化到甚至不需要編寫python代碼就可以編寫應用程序.

### 改良 url

polls/urls.py

```python
from django.urls import path

from . import views

app_name = "polls"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

將`<question_id>`改為`<pk>`, 因為在 `DetailView` 中從 url 獲取的 primary key 叫 “pk”

### 修改 views

polls/views.py

```python
from django.db.models import F
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import Choice, Question

class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"

class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"

def vote(request, question_id):
    # same as above, no changes needed.
    ...
```

所有view都需要知道它該操作的model, 使用 model 屬性提供訊息, 或者透過定義 get_queryset() 方法來實現.

默認情況下 DetailView generic view 使用  **`<app name>/<model name>_detail.html`** 的模板, 然而使用屬性 `template_name`  指定使用特定模板.

在 ListView 使用屬性 `context_object_name` 覆蓋默認 context 變量名 \<object>_list 或 \<model>_list

## Reference

1. [https://docs.djangoproject.com/en/5.1/intro/tutorial04/](https://docs.djangoproject.com/en/5.1/intro/tutorial04/)
