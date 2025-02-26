#----------------------------------
'''
Brute force-
time complexity = o(n**2)
space complexity = O(1)
Hash map -
time complexity = o(n)
space complexity = O(n)
'''
#----------------------------------
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}
        #hash map
        for i, val in enumerate(nums):
            indices[val] = i
        for i, val in enumerate(nums):
            diff = target - val
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]

'''
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target and [i] != [j]:
                    return ([i, j])
'''

