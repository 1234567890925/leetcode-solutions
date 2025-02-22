'''
https://youtu.be/bNvIQI2wAjk?si=6Zz6dpd_s98gNsKK

Input: nums = [1,2,4,6]

Output: [48,24,12,8]

import numpy as np
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        product_arr = []
        for i in range(len(nums)):
            removed_ele = nums.pop(i)
            print('nums = ', nums)
            product = np.prod(nums)
            print('product = ', product)
            product_arr.append(product)
            nums.insert(i, removed_ele)
        return product_arr     
'''

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * (len(nums))
        prefix = 1
        for i in range(len(nums)):
            result[i] =  prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result



sol = Solution()
nums = [1,2,3,4]
res = sol.productExceptSelf(nums)
print(res)

