class Solution {
    public String longestCommonPrefix(String[] strs) {
        String s = strs[0];
        for (int i = 0; i < strs.length; i++) {
            int j = 0;
            int len = Math.min(s.length(), strs[i].length());
            while (j < len && strs[i].charAt(j) == s.charAt(j)){
                j++;
            }

            s = s.substring(0, j);
        }

        return s;
    }
}