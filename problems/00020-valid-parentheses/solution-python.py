"""
20. Valid Parentheses
https://leetcode.com/problems/valid-parentheses/

Time Complexity: O(n)
Space Complexity: O(n)

Tags: string, stack
"""

class Solution:
    def isValid(self, s: str) -> bool:
        """
        使用堆疊來檢查括號是否有效
        
        Args:
            s: 包含括號的字符串
            
        Returns:
            bool: 括號是否有效
        """
        # 建立括號對應關係
        mapping = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for char in s:
            if char in mapping:  # 右括號
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:  # 左括號
                stack.append(char)
        
        return not stack


def test_solution():
    """測試函數"""
    solution = Solution()
    
    test_cases = [
        ("()", True),
        ("()[]{}", True),
        ("(]", False),
        ("([)]", False),
        ("{[]}", True),
        ("", True),
        ("((", False),
        ("))", False),
    ]
    
    for i, (s, expected) in enumerate(test_cases):
        result = solution.isValid(s)
        print(f"Test {i+1}: s='{s}' -> {result} (Expected: {expected})")
        assert result == expected, f"Test {i+1} failed"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
