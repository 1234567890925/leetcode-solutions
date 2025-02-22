from collections import defaultdict
class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        triplets = defaultdict(list)
        addition = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i != j:
                    addition_val = nums[i] + nums[j]
                    addition.append(addition_val)

        print(addition)
sol = Solution()
nums = [-1,0,1,2,-1,-4]
res = sol.threeSum(nums)