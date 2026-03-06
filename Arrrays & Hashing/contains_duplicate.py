"""Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

Example 1:

Input: nums = [1, 2, 3, 3]

Output: true

Example 2:

Input: nums = [1, 2, 3, 4]

Output: false"""

class Solution:
    def hasDuplicate(self, nums):
        hash_set = set()

        for num in nums:
            if num in hash_set:
                return True
            
            hash_set.add(num)
        
        return False


        