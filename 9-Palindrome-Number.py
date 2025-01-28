class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        reversed = str_x[::-1]
        if reversed == str_x:
            return True
        else:
            return False