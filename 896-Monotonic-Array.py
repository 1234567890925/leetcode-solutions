class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        if all(nums[i] <= nums[i+1] for i in range(len(nums)-1)):
            return True
        if all(nums[i] >= nums[i+1] for i in range(len(nums)-1)):
            return True
        else:
            return False