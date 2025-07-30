class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_l, num_zero = 0, 0
        l = 0
        for r in range(len(nums)):

            if nums[r] == 0:
                num_zero += 1

            while num_zero > k:
                if nums[l] == 0:
                    num_zero -= 1
                l += 1

            window_size = r - l + 1
            max_l = max(window_size, max_l)
        return max_l
