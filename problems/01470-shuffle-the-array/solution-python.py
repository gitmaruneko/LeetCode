"""
1470. Shuffle the Array
https://leetcode.com/problems/shuffle-the-array/

Time Complexity: O(n)
Space Complexity: O(n)

Tags: Array
"""

class Solution:
    def solve(self, nums, n):
        output = []
        for i in range(n):
            output.append(nums[i])
            output.append(nums[i + n])
        return output


def test_solution():
    solution = Solution()
    
    test_cases = [
        ([2,5,1,3,4,7], [2,3,5,4,1,7]),
        ([1,2,3,4,4,3,2,1], [1,4,2,3,3,2,4,1])
    ]
    
    for i, (input_data, expected) in enumerate(test_cases):
        result = solution.solve(input_data, len(input_data) // 2)
        print(f"Test {i+1}: input={input_data} -> {result} (Expected: {expected})")
        assert result == expected, f"Test {i+1} failed"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
