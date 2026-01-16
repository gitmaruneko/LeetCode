# LeetCode Python Solutions 🐍

> **個人 LeetCode 刷題記錄專案** - 使用自動化腳本管理和追蹤 Python 解題進度

[![Language](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![LeetCode](https://img.shields.io/badge/LeetCode-Solutions-orange.svg)](https://leetcode.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

這個專案記錄我在 LeetCode 上的練習解題過程，採用極簡化結構設計，專注於 Python 解題。

## 專案結構

```
LeetCode/
├── README.md                    # 專案說明
├── scripts/                    # 自動化腳本
│   ├── create-problem.py       # 快速創建題目
│   ├── update-stats.py         # 更新統計資訊
│   └── migrate-structure.py    # 結構遷移工具
├── templates/                  # 代碼模板
│   └── python/                 # Python 解題模板
└── problems/                   # 題目解答（極簡結構）
    ├── 00001-two-sum/
    │   ├── README.md           # 題目描述、元數據、思路分析
    │   └── solution-python.py  # Python 解法
    ├── 00020-valid-parentheses/
    │   ├── README.md
    │   ├── solution-python.py      # 主要解法：堆疊
    │   └── alt1_counter-python.py  # 替代解法：計數器
    └── ...
```

## ✨ 專案特色

- 🎯 **極簡結構**：每題只有 README + solution-python.py
- 📊 **自動統計**：一鍵更新解題進度和分類索引  
- 🔧 **快速創建**：使用腳本秒速建立新題目結構
- 📚 **智能管理**：YAML frontmatter 整合所有元數據
- 🐍 **Python 專精**：專注 Python 解題和最佳實踐

## 🚀 快速開始

### 創建新題目
```bash
python scripts/create-problem.py 283 "Move Zeroes" easy
```

### 更新統計資訊
```bash
python scripts/update-stats.py
```

## 檔案命名規範

- **題目資料夾**：`{5位數ID}-{kebab-case題名}`
  - 範例：`00020-valid-parentheses`
- **主要解答**：`solution-python.py`
- **替代解法**：`alt{編號}_{關鍵詞}-python.py`
  - 範例：`alt1_stack-python.py`
- **README 包含**：YAML frontmatter 元數據 + Markdown 內容
- **一律小寫、kebab-case**

## 難度分類

- ✅ Easy
- 🟡 Medium  
- 🔴 Hard

## 解題語言

- 🐍 **Python**（主要練習語言）

## 學習資源

- 📚 [Python 練習指南](./docs/python-practice-guide.md) - Python 解題技巧與模板
- 📊 [按難度分類索引](./docs/index-by-difficulty.md) - 題目難度分類
- 🏷️ [按標籤分類索引](./docs/index-by-tags.md) - 題目標籤分類

## 統計資訊

| 難度 | 已解題數 |
|------|----------|
| 🟢 Easy | 4 |
| 🟡 Medium | 0 |
| 🔴 Hard | 0 |
| **總計** | **4** |


## 最近練習

| 題號 | 題目 | 難度 | 完成日期 |
|------|------|------|----------|
| 27 | [Remove Element](./problems/00027-remove-element) | 🟢 Easy | 2026-01-15 |
| 1470 | [Shuffle the Array](./problems/01470-shuffle-the-array) | 🟢 Easy | 2025-12-09 |
| 1408 | [Running Sum of 1d Array](./problems/01408-running-sum-of-1d-array) | 🟢 Easy | 2025-12-05 |
