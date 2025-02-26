#----------------------------------
'''
optimised -
time complexity = o(n) -> string replacement
space complexity = O(n) -> both str_no_space and str_reverse take space in the memory

NO OPTIMIZED SOLUTION FOUND
AN ALTERNATE SOLUTION WITH WHILE IS WRITTER BELOW THE MAIN CODE
'''
#----------------------------------

import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_no_space = re.sub(r"[^a-zA-Z0-9]", "", s).replace(" ", "").lower()
        str_reverse = str_no_space[::-1].lower()
        print(str_reverse)
        if str_no_space != str_reverse:
            return False
        else:
            return True