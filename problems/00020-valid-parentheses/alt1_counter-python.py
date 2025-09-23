"""
20. Valid Parentheses - Alternative Solution: Counter Method
https://leetcode.com/problems/valid-parentheses/

Time Complexity: O(n)
Space Complexity: O(1)

適用於單一類型括號的情況
"""

class Solution:
    def isValid(self, s: str) -> bool:
        """
        使用計數器方法檢查括號（僅適用於單一類型括號）
        這個實現展示了不同的思路，但對於多種括號類型有限制
        
        Args:
            s: 包含括號的字符串
            
        Returns:
            bool: 括號是否有效
        """
        # 檢查是否包含多種括號類型
        bracket_types = set(s) & set('()[]{}\n')
        if len(bracket_types) > 2:  # 如果超過一對括號類型，使用堆疊方法
            return self._stack_method(s)
        
        # 單一類型括號的計數器方法
        count = 0
        left_bracket = None
        right_bracket = None
        
        # 確定括號類型
        for char in s:
            if char in '([{':
                if left_bracket is None:
                    left_bracket = char
                    right_bracket = {'(': ')', '[': ']', '{': '}'}[char]
                elif char != left_bracket:
                    return self._stack_method(s)  # 多種類型，改用堆疊
        
        # 計數器邏輯
        for char in s:
            if char == left_bracket:
                count += 1
            elif char == right_bracket:
                count -= 1
                if count < 0:  # 右括號過多
                    return False
        
        return count == 0
    
    def _stack_method(self, s: str) -> bool:
        """後備的堆疊方法"""
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char in mapping:
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:
                stack.append(char)
        
        return not stack


def test_solution():
    """測試函數"""
    solution = Solution()
    
    test_cases = [
        ("()", True),           # 單一類型
        ("(())", True),         # 單一類型，嵌套
        ("()[]{}", True),       # 多種類型
        ("(]", False),          # 多種類型，不匹配
        ("([)]", False),        # 多種類型，順序錯誤
        ("{[]}", True),         # 多種類型，正確嵌套
        ("", True),             # 空字符串
        ("((", False),          # 單一類型，左括號過多
        ("))", False),          # 單一類型，右括號過多
        ("())", False),         # 單一類型，右括號過多
    ]
    
    for i, (s, expected) in enumerate(test_cases):
        result = solution.isValid(s)
        print(f"Test {i+1}: s='{s}' -> {result} (Expected: {expected})")
        assert result == expected, f"Test {i+1} failed"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
