# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Django 學習專案，跟隨官方教學建立一個投票 (polls) 應用程式。Django 5.1.4 + Python 3.11，資料庫使用 SQLite。

## Commands

所有指令需在 `myproject/` 目錄下執行：

```bash
cd myproject

# 啟動開發伺服器
python manage.py runserver

# 執行測試
python manage.py test polls

# 執行單一測試方法
python manage.py test polls.tests.QuestionModelTests.test_was_published_recently_with_future_question

# 資料庫 migration
python manage.py makemigrations
python manage.py migrate

# 建立 superuser（admin 登入用）
python manage.py createsuperuser

# 進入 Django shell
python manage.py shell
```

## Architecture

```
myproject/
├── mysite/          # 專案設定層
│   ├── settings.py  # 設定：語系 zh-hant、時區 Asia/Taipei、SQLite DB
│   └── urls.py      # 根路由：/polls/, /admin/, /i18n/
├── polls/           # 投票 App
│   ├── models.py    # Question（題目）、Choice（選項，FK → Question）
│   ├── views.py     # Class-based views：IndexView、DetailView、ResultsView + vote()
│   ├── urls.py      # app_name="polls"，namespace 路由
│   ├── admin.py     # QuestionAdmin with ChoiceInline（TabularInline）
│   └── tests.py     # Django TestCase，helper: create_question(text, days)
└── templates/
    └── admin/base_site.html  # 覆寫 Admin header，加入語言切換 selector
```

### URL 結構

| URL | View | Name |
|-----|------|------|
| `/polls/` | `IndexView` | `polls:index` |
| `/polls/<pk>/` | `DetailView` | `polls:detail` |
| `/polls/<pk>/results/` | `ResultsView` | `polls:results` |
| `/polls/<question_id>/vote/` | `vote()` | `polls:vote` |
| `/admin/` | Django Admin | — |
| `/i18n/` | set_language | `set_language` |

### 資料模型

- `Question`：`question_text`、`pub_date`；方法 `was_published_recently()` 判斷是否在 24 小時內發布
- `Choice`：`choice_text`、`votes`（default=0）；透過 `ForeignKey` 關聯 `Question`（CASCADE 刪除）

### 國際化

- 預設語系：繁體中文（`zh-hant`），支援切換英文
- Admin 頁面已加入語言切換下拉選單（`templates/admin/base_site.html`）
- `LocaleMiddleware` 已啟用，路由 `/i18n/` 處理語言切換

### Static Files

- App 層級靜態檔案放在 `polls/static/polls/`（CSS、圖片）
- Template 使用 `{% load static %}` 引入
