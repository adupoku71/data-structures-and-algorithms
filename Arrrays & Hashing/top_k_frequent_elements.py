"""
Given an integer array nums and an integer k, return the k most frequent elements within the array.

The test cases are generated such that the answer is always unique.

You may return the output in any order.

Example 1:

Input: nums = [1,2,2,3,3,3], k = 2

Output: [2,3]
Example 2:

Input: nums = [7,7], k = 1

Output: [7]
"""


# Time: O(nlogn) Space: O(n)
def topKFrequent(nums, k):
    freq = {}

    for num in nums:
        freq[num] = freq.get(num, 0) + 1
        
        
    return [x[0] for x in sorted(freq.items(), key= lambda tup: tup[1])[::-1][:k]]


if __name__ == "__main__":
    nums = [1,2,2,3,3,3] 
    k = 2
    print(topKFrequent(nums, k))