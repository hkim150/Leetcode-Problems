class Solution {
    public int countSubstrings(String s) {
        // expand from the center
        int count = 0;

        for (int i=0; i<s.length()*2+1; i++) {
            int l = Math.floorDiv(i, 2);
            int r = Math.floorDiv(i+1, 2);

            while (l >= 0 && r <= s.length()-1 && s.charAt(l--) == s.charAt(r++)) count++;
        }

        return count;
    }
}