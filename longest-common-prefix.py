# Problem #14
# https://leetcode.com/problems/longest-common-prefix
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.

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