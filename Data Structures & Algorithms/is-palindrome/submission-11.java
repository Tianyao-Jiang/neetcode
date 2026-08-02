class Solution {
    public boolean isPalindrome(String s) {
        int l = 0;
        int r = s.length() - 1;
        while (l < r) {
            while(l < r && !isAlphaNum(s.charAt(l))) {
                l++;
            }
            while(l < r && !isAlphaNum(s.charAt(r))) {
                r--;
            }
            if (Character.toLowerCase(s.charAt(l)) != Character.toLowerCase(s.charAt(r))) {
                return false;
            }
            l++;
            r--;
        }

        return true;
    }

    private boolean isAlphaNum(char c) {
        return (c <= 'z' && c >= 'a') ||
               (c <= 'Z' && c >= 'A') || 
               (c <= '9' && c >= '0');
    }
}
