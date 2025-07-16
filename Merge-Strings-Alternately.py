class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        merged = ""
        i, j = 0, 0
        m, n = len(word1), len(word2)
        while i<m and j<n:
            merged += word1[i]
            merged += word2[i]
            i += 1
            j += 1

        if i<m:
            merged += word1[i:]
        
        if j<n:
            merged += word2[j:]

        return merged