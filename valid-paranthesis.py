'''
Example 1:
Input: s = "[]"

Output: true
Example 2:

Input: s = "([{}])"
(
    [
        {
        }
    ]
)

Output: true
Example 3:

Input: s = "[(])"

Output: false
'''
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {')':'(', ']':'[', '}':'{'}
        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        return True if not stack else False
sol = Solution()
s = "([{}])"
res = sol.isValid(s)
print(res)