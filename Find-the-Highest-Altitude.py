from typing import List
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        alt = 0
        alt_arr = [0]

        for g in gain:
            alt += g
            alt_arr.append(alt)

        return max(alt_arr)
