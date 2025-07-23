from collections import OrderedDict
class Solution:
    def compress(self, chars: List[str]) -> int:

        s = []
        count = 1
        for i in range(1, len(chars)+1):
            if i < len(chars) and chars[i] == chars[i-1]:
                count += 1
            else:
                s.append(chars[i-1])
                if count > 1:
                    s.extend(list(str(count)))
                count = 1
                
        for i in range(len(s)):
            chars[i] = s[i]
        return len(s)
