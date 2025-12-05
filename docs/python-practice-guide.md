# Python LeetCode Practice Guide

## 🐍 Why Choose Python?

- **Concise Syntax**: Focus on algorithm logic rather than syntax details
- **Rich Built-in Functions**: `len()`, `sorted()`, `max()`, `min()`, etc.
- **Powerful Data Structures**: `list`, `dict`, `set`, `deque`, etc.
- **Interview Friendly**: Most companies accept Python solutions

## Common Python Techniques

### 1. List Operations
```python
# List comprehension
squares = [x**2 for x in range(10)]

# Slicing
reversed_list = nums[::-1]

# Two pointers
left, right = 0, len(nums) - 1
```

### 2. Dictionary & Set
```python
# Counter
from collections import Counter
count = Counter(nums)

# Set operations
seen = set()
if num in seen:
    return True
seen.add(num)
```

### 3. Stack & Queue
```python
# Stack (using list)
stack = []
stack.append(item)  # push
item = stack.pop()  # pop

# Queue (using deque)
from collections import deque
queue = deque()
queue.append(item)     # enqueue
item = queue.popleft() # dequeue
```

### 4. Sorting & Searching
```python
# Custom sorting
nums.sort(key=lambda x: x[1])  # Sort by second element

# Binary search
import bisect
index = bisect.bisect_left(nums, target)
```

## Solution Templates

### Basic Template
```python
class Solution:
    def problemName(self, param):
        """
        Approach:
        1. [Step 1]
        2. [Step 2]
        3. [Step 3]
        
        Time: O(?)
        Space: O(?)
        """
        # Implementation
        pass
```

### Test Template
```python
def test_solution():
    solution = Solution()
    
    # Test cases
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

## Practice Suggestions

### Beginner Stage (Easy Problems)
1. **Array & String**: Two Sum, Valid Palindrome
2. **Linked List**: Reverse Linked List, Merge Two Lists
3. **Tree**: Maximum Depth, Same Tree

### Intermediate Stage (Medium Problems)
1. **Dynamic Programming**: Climbing Stairs, House Robber
2. **Graph**: Number of Islands, Course Schedule
3. **Backtracking**: Letter Combinations, Subsets

### Advanced Stage (Hard Problems)
1. **Complex DP**: Edit Distance, Regular Expression
2. **Advanced Data Structures**: LRU Cache, Sliding Window Maximum

## Common Pitfalls

1. **Integer Overflow**: Python automatically handles large integers
2. **Index Range**: Be careful with `range(len(arr))` boundaries
3. **Shallow vs Deep Copy**: Use `copy.deepcopy()` carefully
4. **Dictionary KeyError**: Use `dict.get(key, default)` for safety

## Code Style

- Use **snake_case** for variable and function names
- Add appropriate comments explaining algorithm logic
- Keep functions concise with single responsibility
- Use meaningful variable names

## Quick Problem Creation

```bash
python scripts/create-problem.py <problem_id> "<problem_title>" <difficulty>
```

Example:
```bash
python scripts/create-problem.py 21 "Merge Two Sorted Lists" easy
```

This will automatically create:
- `problems/00021-merge-two-sorted-lists/README.md` (with YAML frontmatter)
- `problems/00021-merge-two-sorted-lists/solution-python.py`

Minimal structure, focus on solving! 🚀
