# Django Learning day 5

## 自動化測試

慣例上, 應用的測試應寫在應用的 test.py 文件內. 測試系統會自動的在所有文件內尋找並執行 test開頭的測試函數.

polls/test.py

```python
import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Question

class QuestionModelTests(TestCase):
    def test_was_published_recently_with_future_question(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """
        time = timezone.now() + datetime.timedelta(days=30)
        future_question = Question(pub_date=time)
        self.assertIs(future_question.was_published_recently(), False)
```

polls/models.py

```python
# ...
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
```

### 測試

```bash
python managy.py test polls
```

運行過程：

- 尋找 polls 應用內的測試代碼
- 找到 django.test.TestCase 的子類
- 為了測試創建一個特殊數據庫
- 尋找 test 開頭的測試函數
- 在 `test_was_published_recently_with_future_question()` 創建了一個 Question 實例,  接著使用 `assertIs()`

## Reference

1. [https://docs.djangoproject.com/zh-hans/5.1/intro/tutorial05/](https://docs.djangoproject.com/zh-hans/5.1/intro/tutorial05/)
