class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        max_candies = max(candies)
        for i in candies:
            total_candies_i_has = i + extraCandies
            if total_candies_i_has >= max_candies:
                res.append(True)
            else:
                res.append(False)
        return res