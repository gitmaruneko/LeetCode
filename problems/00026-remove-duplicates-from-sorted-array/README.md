---
id: 26
title: "Remove Duplicates from Sorted Array"
url_slug: "remove-duplicates-from-sorted-array"
difficulty: "easy"
tags: ['Array', 'Two Pointers']
topics: ['Array', 'Two Pointers']
date_created: "2026-03-31"
date_solved: "2026-03-31"
languages: ['python']
notes: ""
---

# 26. Remove Duplicates from Sorted Array

> **Problem Information**  
> 🔗 [LeetCode](https://leetcode.com/problems/remove-duplicates-from-sorted-array/) | 🎯 🟢 **Easy** | 🏷️ `Array` `Two Pointers` | 📅 2026-03-31

## Intuition 
既然陣列是排序過的, 那麼重複的資料必定相鄰
這表示不需要從頭到尾都搜尋一次
只需要比較相鄰資料
利用兩個指針即可完成在同一陣列進行資料搬動

Since the array is sorted, duplicate elements are guaranteed to be adjacent. This means we don't need a full search; we only need to compare neighboring elements. By using two pointers, we can shift unique elements to the front of the same array in-place.


## Approach

### Method:

1. Handle Edge Case: First, verify that the array is not empty. If it is, return 0 immediately.
2. Initialize Slow Pointer: Set a slow pointer k to index 0, which will track the position for the next unique element.
3. Iterate and Compare: Use a for loop with a fast pointer i (starting from index 1). Compare the value at i with the value at k.
    - If nums[i] is not equal to nums[k], it means a new unique value is found.
    - Increment k and overwrite nums[k] with the value of nums[i].
4. Return Result: Once the loop finishes, return k + 1 as the new length of the unique array.

## Complexity Analysis

### Method
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

## Notes

Add solution notes and insights here
