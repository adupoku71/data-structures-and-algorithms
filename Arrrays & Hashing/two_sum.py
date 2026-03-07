"""

Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.

Example 1:

Input: 
nums = [3,4,5,6], target = 7

Output: [0,1]
"""

# Time: O(n**2) Space: O(1)
def two_sum_brute_force(nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
# Time: O(n) Space: O(n)
def two_sum_optimized(nums, target: int):
        nums_store = {}

        for index, number in enumerate(nums):
            diff = target - number
            if diff in nums_store:
                return [nums_store[diff], index]
            nums_store[number] = index
        