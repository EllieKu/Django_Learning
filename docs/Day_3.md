# Django Learning day 3

## 基本

在 [views.py](http://views.py) 中添加視圖, 在 [urls.py](http://urls.py) 中調用

```python
# polls/views.py

def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
```

```python
# polls/urls.py

#...
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

## 進階

### Views

在應用中創建 templates 目錄, Django 會在此目錄找模板文件.

```html
<!-- polls/templates/polls/index.html -->

{% if latest_question_list %}
    <ul>
    {% for question in latest_question_list %}
        <li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
    {% endfor %}
    </ul>
{% else %}
    <p>No polls are available.</p>
{% endif %}
```

調整 views, 載入 polls/index.html, 並向它傳遞一個 context. The context is a dictionary mapping template variable names to Python objects.

```python
# polls/views.py

from django.http import HttpResponse
from django.template import loader
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    template = loader.get_template("polls/index.html")
    context = {
        "latest_question_list": latest_question_list,
    }
    return HttpResponse(template.render(context, request))
```

A shortcut: render()

將「載入模板, 填充上下文, 再由HttpResponse生成」 操作流程濃縮成 render(), 不再需要導 loader, HttpResponse

```python
# polls/views.py

from django.shortcuts import render
from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)
```

### Raising a 404 error

```python
# polls/views.py

from django.http import Http404
from django.shortcuts import render
from .models import Question

# ...
def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "polls/detail.html", {"question": question})
```

A shortcut: get_object_or_404()

將.get() 和 Http404 濃縮成 get_object_or_404()

**pk** stands for “primary key”

```python
from django.shortcuts import get_object_or_404, render
from .models import Question

# ...
def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "polls/detail.html", {"question": question})
```

## Removing hardcoded URLs in templates

透過使用 {% url %}  在 pools.urls 中 url 定義中尋找指定名字, 消除特定 url 路徑的依賴,

原先：

```html
<!-- polls/templates/polls/index.html -->

<li><a href="/polls/{{ question.id }}/">{{ question.question_text }}</a></li>
```

修改：

```html
<!-- polls/templates/polls/index.html -->

<li><a href="{% url 'detail' question.id %}">{{ question.question_text }}</a></li>
```

## Namespacing URL names

若有不同應用但重名的url, Django 如何得知 {% url %} 對應哪個應用的url ?

故在 URLconf 中增加 namespaces

```python
# polls/urls.py

from django.urls import path
from . import views

#add
app_name = "polls"
urlpatterns = [
    path("", views.index, name="index"),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
```

```html
<!-- polls/templates/polls/index.html -->

<li><a href="{% url 'polls:detail' question.id %}">{{ question.question_text }}</a></li>
```
