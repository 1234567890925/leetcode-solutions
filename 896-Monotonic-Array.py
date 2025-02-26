#----------------------------------
'''
Time Complexity: O(n) - Iterates through the list at most twice.
Space Complexity: O(1) - Uses only a constant amount of extra space.
'''
#----------------------------------
class Solution:
    def isMonotonic(self, nums: list[int]) -> bool:
        if all(nums[i] <= nums[i+1] for i in range(len(nums)-1)):
            return True
        if all(nums[i] >= nums[i+1] for i in range(len(nums)-1)):
            return True
        else:
            return False