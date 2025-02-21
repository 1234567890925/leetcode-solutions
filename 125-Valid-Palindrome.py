import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        str_no_space = re.sub(r\[^a-zA-Z0-9]\, \\, s).replace(\ \, \\).lower()
        str_reverse = str_no_space[::-1].lower()
        print(str_reverse)
        if str_no_space != str_reverse:
            return False
        else:
            return True