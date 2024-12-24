## Init first project

創建專案名叫 *mysite* 在資料夾 *day_1* 下

```bash
$ django-admin startproject mysite day_1
```

進入 day_1 資料夾, 啟動專案

```bash
$ python manage.py runserver
```

網頁運行在 http://127.0.0.1:8000

## Creating app

在與 [manage.py](http://manage.py) 同路徑下創建app名叫 *polls:*

```bash
$ python manage.py startapp polls
```

<aside>
❓

Project vs App

app 是一個應用程式, 可以在很多個 project 內; project 是特定網站的配置和應用程式的集合, 一個 project 內可以包含多個app

</aside>

### Step 1 -  加入 views

polls/views.py

```python
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
```

### Step 2 - 創建 urls

polls/urls.py

```python
from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
]
```

### Step 3 - 修改專案設定

mysite/urls.py

```python
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
```

啟動專案遇到報錯

> You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python [manage.py](http://manage.py/) migrate' to apply them.
> 

執行 `$ python manage.py migrate`  

http://127.0.0.1:8000/polls/