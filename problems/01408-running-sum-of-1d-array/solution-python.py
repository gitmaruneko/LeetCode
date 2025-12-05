"""
1408. Running Sum of 1d Array
https://leetcode.com/problems/running-sum-of-1d-array/

Time Complexity: O(N)
Space Complexity: O(N)

Tags: list
"""

class Solution:
    def solve(self, param):

        list_running_sum = []
        current_sum = 0
        for num in param:
            current_sum += num
            list_running_sum.append(current_sum)
        return list_running_sum
        


def test_solution():
    """測試函數"""
    solution = Solution()
    
    test_cases = [
        ([1,2,3,4], [1,3,6,10]),([1,1,1,1,1], [1,2,3,4,5]),([3,1,2,10,1], [3,4,6,16,17])
    ]
    
    for i, (input_data, expected) in enumerate(test_cases):
        result = solution.solve(input_data)
        print(f"Test {i+1}: input={input_data} -> {result} (Expected: {expected})")
        assert result == expected, f"Test {i+1} failed"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
