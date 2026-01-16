"""
27. Remove Element
https://leetcode.com/problems/remove-element/

Time Complexity: O(?)
Space Complexity: O(?)

Tags: Array, Two Pointers
"""

class Solution:
    def solve(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
                
        return k


def test_solution():
    solution = Solution()
    
    test_cases = [
        (([3,2,2,3], 3), 2),  # ((nums, val), expected_k)
        (([0,1,2,2,3,0,4,2], 2), 5)
    ]
    
    for i, (input_data, expected) in enumerate(test_cases):
        nums, val = input_data  # Unpack nums and val
        result = solution.solve(nums, val)
        print(f"Test {i+1}: nums={nums[:result]}, k={result} (Expected k: {expected})")
        assert result == expected, f"Test {i+1} failed"
    
    print("All tests passed!")


if __name__ == "__main__":
    test_solution()
