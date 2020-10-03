class Solution {
    public int firstUniqChar(String s) {
        int[] count = new int[26];
        for (int i=0; i<s.length(); i++) {
            count[(int)s.charAt(i) - (int)'a']++;
        }

        for (int i=0; i<s.length(); i++) {
            if (count[(int)s.charAt(i) - (int)'a'] == 1)
                return i;
        }

        return -1;
    }
}