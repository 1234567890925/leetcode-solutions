class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = set(list('AaEeIiOoUu'))
        s = list(s)
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] in vowels and s[right] in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            if s[left] not in vowels:
                left += 1
            if s[right] not in vowels:
                right -= 1
        return ''.join(s)

#brute force:
'''
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join(reversed(s.split()))
'''
