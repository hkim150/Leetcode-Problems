class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length())
            return false;

        int[] cnt = new int[26];

        for (int i=0; i<s.length(); i++) {
            cnt[(int)s.charAt(i) - (int)'a']++;
            cnt[(int)t.charAt(i) - (int)'a']--;
        }

        for (int i=0; i<cnt.length; i++) {
            if (cnt[i] != 0)
                return false;
        }

        return true;
    }
}