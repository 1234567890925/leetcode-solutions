from collections import defaultdict
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = defaultdict(int)
        for i in arr:
            counts[i] += 1
        occur = list(counts.values())
        if len(occur) != len(set(occur)):
            return False
        return True