class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return \\
        prefix_str = strs[0]

        for i in range(1, len(strs)):
            for j in range(min(len(prefix_str), len(strs[i]))):
                if prefix_str[j] != strs[i][j]:
                    prefix_str = prefix_str[:j]
                    break
            prefix_str = prefix_str[:len(strs[i])]
            if not prefix_str:
                return \\
        return prefix_str