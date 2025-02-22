class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums_sort = sorted(set(nums))
        count = 1
        max_count = 1
        if not nums:
            return 0
        for i in range(1, len(nums_sort)):
            if nums_sort[i] == nums_sort[i-1] + 1:
                count += 1
            else:
                max_count = max(max_count, count)
                count = 1
        max_count = max(max_count, count)
        return max_count