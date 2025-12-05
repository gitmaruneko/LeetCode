---
id: 1408
title: "Running Sum of 1d Array"
url_slug: "running-sum-of-1d-array"
difficulty: "easy"
tags: ['list', 'sum']
topics: ["data-structures"]
date_created: "2025-12-05"
date_solved: "2025-12-05"
languages: ['python']
notes: ""
related_problems:
  - id: 1408
    title: "相關題目1"
  - id: 1408
    title: "相關題目2"
---

# 1408. Running Sum of 1d Array

> **題目資訊**  
> 🔗 [LeetCode](https://leetcode.com/problems/running-sum-of-1d-array/) | 🎯 🟢 **Easy** | 🏷️ `list` `sum` | 📅 2025-12-05

## 題目描述

給定一個整數陣列,計算出動態和
動態和的定義是: 在數組的第i個位置上, 其值是從開頭道第i個位置的所有元素的總和

## 解題思路

### 方法一：

1. 建立一個新的空LIST
2. 設定一個變數用來存放開頭至i-1的總和
3. 從傳入的字串中取出數值相加, 放入List
4. 回傳List最終結果

## 複雜度分析

### 方法一
- **時間複雜度**：O(N)
- **空間複雜度**：O(N)

## 學習筆記


