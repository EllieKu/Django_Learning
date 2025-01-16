# Django Learning day 6

## Static Resource

在應用下創建一個 **static** 的目錄, Django 將在該目錄下尋找靜態文件（與template類似）

polls/static/polls/style.css

```css
li a {
    color: green;
}
```

polls/templates/polls/index.html

```html
{% load static %}

<link rel="stylesheet" href="{% static 'polls/style.css' %}">

```

`{% static %}` 會生成靜態文件的絕對路徑. Django 會將 {% static ‘polls/style.css’ %} 轉換基於 [STATIC_URL](https://docs-djangoproject-com.translate.goog/en/5.1/ref/settings/?_x_tr_sl=en&_x_tr_tl=zh-TW&_x_tr_hl=zh-TW&_x_tr_pto=sc#std-setting-STATIC_URL) 設定的路徑: /static/polls/style.css. 若檔案的非由 Django 生成則無法直接引用.

## Reference

1. [https://docs-djangoproject-com.translate.goog/en/5.1/intro/tutorial06/?_x_tr_sl=en&_x_tr_tl=zh-TW&_x_tr_hl=zh-TW&_x_tr_pto=sc](https://docs-djangoproject-com.translate.goog/en/5.1/intro/tutorial06/?_x_tr_sl=en&_x_tr_tl=zh-TW&_x_tr_hl=zh-TW&_x_tr_pto=sc)
