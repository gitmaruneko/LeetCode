---
id: 27
title: "Remove Element"
url_slug: "remove-element"
difficulty: "easy"
tags: ['Array', 'Two Pointers']
topics: ['Array', 'Two Pointers']
date_created: "2026-01-15"
date_solved: "2026-01-15"
languages: ['python']
notes: "Add notes here"
---

# 27. Remove Element

> **Problem Information**  
> 🔗 [LeetCode](https://leetcode.com/problems/remove-element/) | 🎯 🟢 **Easy** | 🏷️ `Array` `Two Pointers` | 📅 2026-01-15

## Intuition 
The challenge is to remove elements in-place without allocating extra space. I realized that instead of literally 'deleting' elements (which is expensive in an array), I can simply overwrite the elements we want to discard by shifting the elements we want to keep to the front of the array using two pointers.

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

## Approach

### Method 1:

1. Initialize a slow pointer k at index 0.
2. Iterate through the array with a fast pointer i.
3. If nums[i] is NOT equal to val:
   Assign nums[i] to nums[k].
   Move the slow pointer k forward by 1.
4. Continue moving i until the end of the list.
5. Return k (the new length).

## Complexity Analysis

### Method
- **Time Complexity**: O(n)
- **Space Complexity**: O(1)

## Notes

Add solution notes and insights here
