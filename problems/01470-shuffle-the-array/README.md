---
id: 1470
title: "Shuffle the Array"
url_slug: "shuffle-the-array"
difficulty: "easy"
tags: ['Array']
topics: ['Array']
date_created: "2025-12-09"
date_solved: "2025-12-09"
languages: ['python']
notes: "Add notes here"
---

# 1470. Shuffle the Array

> **Problem Information**  
> 🔗 [LeetCode](https://leetcode.com/problems/shuffle-the-array/) | 🎯 🟢 **Easy** | 🏷️ `Array` | 📅 2025-12-09

## Problem Description

Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Return the array in the form [x1,y1,x2,y2,...,xn,yn].

## Approach

### Method 1:

1. Initialization: Create an empty list (or array) named output.
2. Pattern Analysis: Observe that each pair of elements consists of nums[i] and nums[i+n].
3. Iteration: Run a loop through range(n), appending these two corresponding values sequentially in each iteration.

## Complexity Analysis

### Method
- **Time Complexity**: O(n)
- **Space Complexity**: O(n)

## Notes

Add solution notes and insights here
