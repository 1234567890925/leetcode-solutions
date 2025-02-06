class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_new = defaultdict(list)
        for word in strs:
            sorted_word = "".join(sorted(word))
            reversed_word = sorted_word[::-1]
            strs_new[sorted_word].append(word)
        return list(strs_new.values())