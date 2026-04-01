---
id: 283
title: "Move Zeroes"
url_slug: "move-zeroes"
difficulty: "easy"
tags: ['Array', 'Two Pointers']
topics: ['Array', 'Two Pointers']
date_created: "2026-04-01"
date_solved: "2026-04-01"
languages: ['python']
notes: ""
---

# 283. Move Zeroes

> **Problem Information**  
> 🔗 [LeetCode](https://leetcode.com/problems/move-zeroes/) | 🎯 🟢 **Easy** | 🏷️ `Array` `Two Pointers` | 📅 2026-04-01

## Intuition 
To maintain the relative order of non-zero elements, we must process the array from left to right. Using two pointers moving in the same direction allows us to "collect" non-zero values and place them at the beginning of the array sequentially, while pushing zeros to the remaining slots.


## Approach

### Method:

1. Initialize: Set a slow pointer k = 0 to represent the next position to fill with a non-zero element.
2. Iterate: Use a fast pointer i to scan from index 0 to the end.
    - Action: Whenever nums[i] is not zero, we want to bring it forward.
    - Option A (Overwrite): Copy nums[i] to nums[k] and increment k. (Then fill the rest with 0 later).
    - Option B (Swap): Swap nums[i] and nums[k], then increment k. (This pushes zeros back automatically).
3. Result: The array is modified in-place with all zeros at the end.

## Complexity Analysis

### Method
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

## Notes

Add solution notes and insights here
