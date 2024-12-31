# Django Learning day 2

本章在設置數據庫, 並創建模型

## Settings

模組設定在 *mysite/settings.py,* 其中 `INSTALLED_APPS` 是保存實例中啟動的所有應用程序名稱.

預設情況下包含下列應用：

- [**`django.contrib.admin`**](https://docs.djangoproject.com/en/5.1/ref/contrib/admin/#module-django.contrib.admin)– 管理網站。
- [**`django.contrib.auth`**](https://docs.djangoproject.com/en/5.1/topics/auth/#module-django.contrib.auth)– 身份驗證系統。
- [**`django.contrib.contenttypes`**](https://docs.djangoproject.com/en/5.1/ref/contrib/contenttypes/#module-django.contrib.contenttypes)– 內容類型框架。
- [**`django.contrib.sessions`**](https://docs.djangoproject.com/en/5.1/topics/http/sessions/#module-django.contrib.sessions)– 會話框架。
- [**`django.contrib.messages`**](https://docs.djangoproject.com/en/5.1/ref/contrib/messages/#module-django.contrib.messages)– 訊息傳遞框架。
- [**`django.contrib.staticfiles`**](https://docs.djangoproject.com/en/5.1/ref/contrib/staticfiles/#module-django.contrib.staticfiles)– 管理靜態文件的框架。

## Migrate

**migrate** 命令是查看`INSTALLED_APPS` 設定, 並根據 *mysite/settings.py* 的內容建立任何必要的資料庫表

```bash
python manage.py migrate
```

## Creating models

在 Django 中寫一個數據庫驅動的 web 應用的第一步是定義模型

### Step1 - 建立 models

polls/models.py

```python
from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
```

### Step2 - 啟動

在`INSTALLED_APPS` 設定加入其應用配置的引用. 配置物件 `PollsConfig` 在 polls/app.py.

mysite/settings.py

```python
INSTALLED_APPS = [
    "polls.apps.PollsConfig",
    ...
]
```

接下來, 透過運行 ***makemigrations***,  Django 會檢測 models 的變動生成 migrations.  migrations 是 Django 對於模型定義的變化的儲存.

### Step3 - 運行 makemigrations

執行:

```bash
python manage.py makemigrations polls
```

輸出:

```text
Migrations for 'polls':
  polls/migrations/0001_initial.py
    + Create model Question
    + Create model Choice
```

## 與數據庫互動

進入 Python shell , 使用 [數據庫API](https://docs.djangoproject.com/zh-hans/5.1/topics/db/queries/)

```bash
pathon manage.py shell
```

## 創建管理員帳號

```bash
python manage.py createsuperuser
```

輸入帳號、信箱、密碼.

啟動服務器

```bash
python manage.py runserver
```

進入管理頁面  [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin/)

## Reference

1. [https://docs.djangoproject.com/zh-hans/5.1/intro/tutorial02/](https://docs.djangoproject.com/zh-hans/5.1/intro/tutorial02/)
