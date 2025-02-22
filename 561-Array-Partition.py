class Solution:
    def arrayPairSum(self, nums: list[int]) -> int:
        sorted_nums = nums.sort()
        pairs = []
        min_sum = 0
        for i in range(0, len(nums), 2):
            pairs.append((nums[i], nums[i+1]))
        for j, k in pairs:
            min_sum += j
        return min_sum
    
# Time complexity is O(nlogn) as sorting (merge sort) takes O(nlogn)
# [  O(logn) for splitting the elements AND
#    O(n) for merging the elements together]

# Space complexity is O(n) as we are just using the same array