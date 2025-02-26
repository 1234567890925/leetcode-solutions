#----------------------------------
'''
iterative -
time complexity = o(n) -> set checks each item once
space complexity = O(n) -> set
'''
#----------------------------------
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) != len(set(nums)):
            return True
        return False