#----------------------------------
'''
Time Complexity: O(n) - Iterates through the list once.
Space Complexity: O(1) - Uses only a constant amount of extra space.
'''
#----------------------------------
class Solution:
    def isArraySpecial(self, nums: list[int]) -> bool:
        if len(nums) == 1:
            return True
        for i in range(len(nums)-1):
            if nums[i] % 2 == nums[i + 1] % 2:
                return False
        else:
            return True  