"""
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/

Time Complexity: O(n)
Space Complexity: O(1)

Tags: Array, Two Pointers
"""

class Solution:
    time_complexity = "O(n)"
    space_complexity = "O(1)"

    def solve(self, nums):
        k = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[k], nums[i] = nums[i], nums[k]
                k += 1
        return nums


import sys as _sys, pathlib as _pl
_sys.path.insert(0, str(_pl.Path(__file__).parents[2]))
from lc_utils import analyze_complexity as _analyze_complexity


def test_solution():
    """
    Test cases for the solution.
    
    Format examples:
    - Single parameter: (input_value, expected_output)
    - Multiple parameters: ((param1, param2), expected_output)
    - List modification: ((list_input, value), expected_output)
    
    Example formats:
        Single input:    ([1,2,3], 6)
        Two inputs:      (([1,2,3], 2), True)
        Three inputs:    ((nums, target, k), result)
    """
    solution = Solution()
    
    test_cases = [
        ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0]),
        ([0], [0]),
    ]
    
    for i, (input_data, expected) in enumerate(test_cases):
        if isinstance(input_data, tuple):
            result = solution.solve(*input_data)
        else:
            result = solution.solve(input_data)
        print(f"Test {i+1}: input={input_data} -> {result} (Expected: {expected})")
        assert result == expected, f"Test {i+1} failed"

    # Auto-analyze and update complexity in file header
    import re as _re, pathlib as _pl
    tc, sc = _analyze_complexity(Solution.solve)
    _path = _pl.Path(__file__)
    _text = _path.read_text(encoding='utf-8')
    _text = _re.sub(r'^( {4}time_complexity = ")[^"]*"', r'\g<1>' + tc + '"', _text, flags=_re.MULTILINE)
    _text = _re.sub(r'^( {4}space_complexity = ")[^"]*"', r'\g<1>' + sc + '"', _text, flags=_re.MULTILINE)
    _text = _re.sub(r'Time Complexity: O\([^)]*\)', 'Time Complexity: ' + tc, _text)
    _text = _re.sub(r'Space Complexity: O\([^)]*\)', 'Space Complexity: ' + sc, _text)
    _path.write_text(_text, encoding='utf-8')
    print('✅ Complexity updated → Time: %s, Space: %s' % (tc, sc))

    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
