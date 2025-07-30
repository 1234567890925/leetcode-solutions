class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        zero = -1
        l = 0
        max_l = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                l = zero + 1
                zero = r
            max_l = max(max_l, r-l)
        return max_l