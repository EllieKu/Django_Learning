---
name: vcommit
description: 自動分析 git diff，產生符合 conventional commits 格式的 commit message 並完成 commit
---

# Vcommit Skill

自動執行 `git add`、根據 diff 內容判斷 commit 類型，產生 conventional commit message 並提交。

## 執行流程

### Step 1：確認有變更

```bash
git status
git diff --staged
git diff
```

若無任何變更（untracked 或 modified），告知使用者並停止。

### Step 2：分析變更，判斷 commit type

讀取 `git diff HEAD`（含已 staged 與未 staged），根據以下規則判斷 type：

| Type | 判斷條件（優先順序由高到低）|
|------|--------------------------|
| `feat` | 新增功能、新檔案（非測試、非文件）|
| `fix` | 修正 bug、錯誤邏輯修正 |
| `docs` | 只改動 `.md`、`docs/`、`CLAUDE.md`、`requirements.txt` 等文件 |
| `test` | 只改動 `tests.py`、`test_*.py`、`*_test.py` |
| `refactor` | 程式碼重構（無新功能、無 bug fix）|
| `style` | 格式調整（空白、縮排、無邏輯變更）|
| `chore` | 設定檔、`.gitignore`、依賴更新等維護任務 |
| `perf` | 效能改善 |

**多類型變更**：以影響最大的 type 為主，或拆成多行 body 說明。

### Step 3：產生 commit message

格式：
```
<type>(<scope>): <subject>
  - type: 代表 commit 的類別：feat, fix, docs, style, refactor, test, chore，必要欄位。
  - scope 代表 commit 影響的範圍，例如資料庫、控制層、模板層等等，視專案不同而不同，為可選欄位。
  - subject 代表此 commit 的簡短描述，不要超過 50 個字元，結尾不要加句號，為必要欄位。
```

範例：
```
feat: 新增投票功能
```

### Step 4：執行 commit

```bash
# 加入所有變更
git add -A

# 執行 commit
git commit -m "<generated message>"
```

### Step 5：回報結果

顯示：
- commit hash
- commit message
- 變更的檔案清單

## 注意事項

- **不自動 push**，除非使用者明確要求
- 若 `.gitignore` 已排除上述檔案，`git add -A` 即安全
- 遇到 pre-commit hook 失敗時，修正問題後重新 commit（不用 `--no-verify`）
- 使用繁體中文

## 使用方式

使用者說：`/vcommit` 或「幫我 commit」、「自動 commit」

Claude 應：
1. 執行上述流程
2. 將產生的 message 先展示給使用者確認（若使用者要求自動執行則略過確認）
3. 執行 commit 並回報結果
