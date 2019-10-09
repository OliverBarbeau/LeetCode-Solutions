# Given a positive integer, return its corresponding column title as appear in an Excel sheet.

# For example:

#     1 -> A
#     2 -> B
#     3 -> C
#     ...
#     26 -> Z
#     27 -> AA
#     28 -> AB 
#     ...
# Example 1:

# Input: 1
# Output: "A"
# Example 2:

# Input: 28
# Output: "AB"
# Example 3:

# Input: 701
# Output: "ZY"


class Solution {
    public String convertToTitle(int n) {
        String build = "";
        while (n >= 1){
            char ch = (char) (((n-1)%26) + 65);
            build = ch + build;
            n = (n-1) / 26;
        }
        return build;
        //loop modding by 26, add coresponding letter to a built string
    }
}