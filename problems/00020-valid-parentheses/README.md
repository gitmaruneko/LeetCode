---
id: 20
title: "Valid Parentheses"
url_slug: "valid-parentheses"
difficulty: "easy"
tags: ["string", "stack"]
topics: ["data-structures", "string-manipulation"]
date_created: "2025-09-23"
date_solved: "2025-09-23"
languages: ["python"]
notes: "經典的堆疊應用題目，需要注意括號的配對順序。可以用不同方法實現，堆疊是最直觀的解法。"
related_problems:
  - id: 22
    title: "Generate Parentheses"
  - id: 32
    title: "Longest Valid Parentheses"
---

# 20. Valid Parentheses

> **題目資訊**  
> 🔗 [LeetCode](https://leetcode.com/problems/valid-parentheses/) | 🎯 🟢 **Easy** | 🏷️ `string` `stack` | 📅 2025-09-23

## 題目描述

給定一個只包括 `'('`，`')'`，`'{'`，`'}'`，`'['`，`']'` 的字符串 `s`，判斷字符串是否有效。

有效字符串需滿足：
1. 左括號必須與相同類型的右括號閉合
2. 左括號必須與相同類型的右括號正確配對
3. 每個右括號都有一個對應的相同類型的左括號

**範例 1:**
```
輸入: s = "()"
輸出: true
```

**範例 2:**
```
輸入: s = "()[]{}"
輸出: true
```

**範例 3:**
```
輸入: s = "(]"
輸出: false
```

## 解題思路

### 方法一：堆疊 (Stack)

使用堆疊來匹配括號：
1. 遍歷字符串中的每個字符
2. 如果是左括號 `(`、`{`、`[`，則推入堆疊
3. 如果是右括號 `)`、`}`、`]`，檢查堆疊頂部是否為對應的左括號
4. 如果匹配，彈出堆疊頂部；否則返回 false
5. 最終檢查堆疊是否為空

**算法步驟：**
1. 建立括號對應關係的字典
2. 初始化空堆疊
3. 遍歷字符串，根據字符類型執行相應操作
4. 返回堆疊是否為空的結果

### 方法二：計數器 (適用於單一類型括號)

對於只有一種括號的情況，可以使用計數器方法。

## 複雜度分析

### 方法一：堆疊
- **時間複雜度**：O(n) - 需要遍歷字符串一次
- **空間複雜度**：O(n) - 最壞情況下需要存儲所有左括號

### 方法二：計數器
- **時間複雜度**：O(n) - 遍歷字符串一次
- **空間複雜度**：O(1) - 只需要常數額外空間

## 相關標籤

- String
- Stack
- Data Structures

## 相關題目

- [22. Generate Parentheses](https://leetcode.com/problems/generate-parentheses/)
- [32. Longest Valid Parentheses](https://leetcode.com/problems/longest-valid-parentheses/)

## 注意事項

1. 空字符串被認為是有效的
2. 需要處理字符串長度為奇數的情況（必然無效）
3. 注意括號的配對順序，如 `"([)]"` 是無效的


## 學習筆記

經典的堆疊應用題目，需要注意括號的配對順序。
可以用不同方法實現，堆疊是最直觀的解法。
