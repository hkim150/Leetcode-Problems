class Solution {
    // expand around the center
    public String longestPalindrome(String s) {
        int max_length = 0;
        String max_string = "";
        for (int i=0; i<s.length() * 2 - 1; i++) {
            int l = Math.floorDiv(i, 2);
            int r = Math.floorDiv(i+1, 2);

            while (l >= 0 && r < s.length() && s.charAt(l) == s.charAt(r)) {
                if (r - l + 1 > max_length) {
                    max_length = r - l + 1;
                    max_string = s.substring(l, r+1);
                }
                l--;
                r++;
            }
        }

        return max_string;
    }
}