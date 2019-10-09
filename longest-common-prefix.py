class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if strs == []:
            return ""
        length = len(strs[0])
        for word in strs:
            conWord = strs[0][0:length]
            while (length > len(word) or strs[0][0:length] != word[0:length]):
                length -= 1
        return strs[0][0:length]