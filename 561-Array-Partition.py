class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        sorted_nums = nums.sort()
        pairs = []
        min_sum = 0
        for i in range(0, len(nums), 2):
            pairs.append((nums[i], nums[i+1]))
        for j, k in pairs:
            min_sum += j
        return min_sum