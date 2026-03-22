"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in 
O(n)
O(n) time without using the division operation?

Example 1:

Input: nums = [1,2,4,6]

Output: [48,24,12,8]
Example 2:

Input: nums = [-1,0,1,2,3]

Output: [0,-6,0,0,0]
"""


class Solution:
    # Time: O(n**2) Space: O(n)
    def productExceptSelfNaiveSolution(self, nums):
        n = len(nums)
        result = [0] * n

        for i in range(n):
            prod = 1
            for j in range(n):
                if i != j:
                    prod *= nums[j]
            result[i] = prod
        return result
    # Time: O(n) Space: O(n) for postfix and prefix arrays, O(n) for output array
    def productExceptSelfPrefixPostfix(self, nums):
        n = len(nums)
        postfix = [0] * n
        prefix = [0] * n

        prod_pre = 1
        prod_post = 1
        for i in range(n):
            prod_pre *= nums[i]
            prod_post *= nums[n-1-i]
            prefix[i] = prod_pre
            postfix[n-i-1] = prod_post

        output = [0] * n
        for j in range(n):
            pre = 1 if j == 0 else prefix[j-1]
            post = 1 if j == n - 1 else postfix[j + 1]
            output[j] = pre * post
        return output
        