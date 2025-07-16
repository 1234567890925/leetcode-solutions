class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        result = []
        for i in range(0, len(candies)):
            new_c = candies[i] + extraCandies
            if new_c >= max(candies):
                result.append(True)
            else:
                result.append(False)
        return result
