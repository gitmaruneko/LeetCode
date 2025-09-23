# Python LeetCode 練習指南

## 🐍 為什麼選擇 Python？

- **語法簡潔**：專注於算法邏輯而非語法細節
- **豐富的內建函數**：`len()`, `sorted()`, `max()`, `min()` 等
- **強大的資料结構**：`list`, `dict`, `set`, `deque` 等
- **面試友好**：大多數公司接受 Python 解題

## 常用 Python 技巧

### 1. 列表操作
```python
# 列表推導式
squares = [x**2 for x in range(10)]

# 切片操作
reversed_list = nums[::-1]

# 雙指針
left, right = 0, len(nums) - 1
```

### 2. 字典與集合
```python
# 計數器
from collections import Counter
count = Counter(nums)

# 集合操作
seen = set()
if num in seen:
    return True
seen.add(num)
```

### 3. 堆疊與佇列
```python
# 堆疊（使用 list）
stack = []
stack.append(item)  # push
item = stack.pop()  # pop

# 佇列（使用 deque）
from collections import deque
queue = deque()
queue.append(item)     # enqueue
item = queue.popleft() # dequeue
```

### 4. 排序與搜尋
```python
# 自定義排序
nums.sort(key=lambda x: x[1])  # 按第二個元素排序

# 二分搜尋
import bisect
index = bisect.bisect_left(nums, target)
```

## 解題模板

### 基本模板
```python
class Solution:
    def problemName(self, param):
        """
        解題思路：
        1. [步驟1]
        2. [步驟2]
        3. [步驟3]
        
        Time: O(?)
        Space: O(?)
        """
        # 實現邏輯
        pass
```

### 測試模板
```python
def test_solution():
    solution = Solution()
    
    # 測試案例
    test_cases = [
        (input1, expected1),
        (input2, expected2),
    ]
    
    for i, (input_data, expected) in enumerate(test_cases):
        result = solution.problemName(input_data)
        print(f"Test {i+1}: {result} == {expected}")
        assert result == expected
    
    print("All tests passed! ✅")
```

## 練習建議

### 新手階段（Easy 題目）
1. **陣列與字串**：Two Sum, Valid Palindrome
2. **鏈表**：Reverse Linked List, Merge Two Lists
3. **樹**：Maximum Depth, Same Tree

### 進階階段（Medium 題目）
1. **動態規劃**：Climbing Stairs, House Robber
2. **圖論**：Number of Islands, Course Schedule
3. **回溯**：Letter Combinations, Subsets

### 高級階段（Hard 題目）
1. **複雜 DP**：Edit Distance, Regular Expression
2. **高級資料結構**：LRU Cache, Sliding Window Maximum

## 常見陷阱

1. **整數溢出**：Python 自動處理大整數
2. **索引範圍**：注意 `range(len(arr))` 的邊界
3. **淺拷貝 vs 深拷貝**：使用 `copy.deepcopy()` 時要小心
4. **字典的 KeyError**：使用 `dict.get(key, default)` 更安全

## 程式碼風格

- 使用 **snake_case** 命名變數和函數
- 適當的註釋說明算法思路
- 保持函數簡潔，單一職責
- 使用有意義的變數名

## 快速創建新題目

```bash
python scripts/create-problem.py <題號> "<題目名稱>" <難度>
```

範例：
```bash
python scripts/create-problem.py 21 "Merge Two Sorted Lists" easy
```

這將自動創建：
- `problems/00021-merge-two-sorted-lists/README.md` (包含 YAML frontmatter)
- `problems/00021-merge-two-sorted-lists/solution-python.py`

極簡結構，專注解題！ 🚀
