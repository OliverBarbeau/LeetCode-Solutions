// Problem #171
// https://leetcode.com/problems/excel-sheet-column-number
// # Given a column title as appear in an Excel sheet, return its corresponding column number.

// # For example:

// #     A -> 1
// #     B -> 2
// #     C -> 3
// #     ...
// #     Z -> 26
// #     AA -> 27
// #     AB -> 28 
// #     ...
// # Example 1:

// # Input: "A"
// # Output: 1
// # Example 2:

// # Input: "AB"
// # Output: 28
// # Example 3:

// # Input: "ZY"
// # Output: 701

class Solution {
    public int titleToNumber(String s) {
        //take string 
        int sum = 0;
        int len = s.length();
        int back = 1;
        int num;
        for (int n = len-1; n >= 0; n--){
            num = (int) s.charAt(n);
            //System.out.println("\nNum:");

            //System.out.println(num);

            num -= 64;
            //System.out.println(num);

            sum += (back * num);
            //System.out.println("\nSum:");
            //System.out.println(sum);
            back *= 26;
        }
        return sum;
    }
}
