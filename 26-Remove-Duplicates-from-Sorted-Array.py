#----------------------------------
'''
Brute force -
time complexity = o(n) -> 1 loop
space complexity = O(1)

NO OPTIMIZED SOLUTION FOUND
AN ALTERNATE SOLUTION WITH WHILE IS WRITTER BELOW THE MAIN CODE
'''
#----------------------------------
# Brute force - 
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        j = 0
        for i in range(1, len(nums)):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]  
        return j+1

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:  # Handle the case where the input list is empty
            return 0

        j = 0
        i = 1
        while i < len(nums):
            if nums[j] != nums[i]:
                j += 1
                nums[j] = nums[i]
            i += 1
        return j + 1
