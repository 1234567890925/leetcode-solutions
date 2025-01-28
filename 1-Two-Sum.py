class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in new_dict:
                return [new_dict[complement], i]
            else:
                new_dict[num] = i
        