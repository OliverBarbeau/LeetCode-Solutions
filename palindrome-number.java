class Solution {
    public boolean isPalindrome(int x) {
        //use mod 10 to grab last digit
        //how do you simultaniously grab first digit
        if (x < 0){
            return false;
        }
        int copy = x;
        int lastPos = 0;
        int[] digits = new int[10];
        while (copy >= 10){
            digits[lastPos] = copy % 10;
            lastPos += 1;
            copy /= 10;
        }
        digits[lastPos] = copy % 10;
        
        int limit = lastPos / 2;
        for (int i = 0; i <= limit; i++){
            if (digits[i] != digits[lastPos-i]){
                return false;
            }
        }
        return true;
    }
    
}