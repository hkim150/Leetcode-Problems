class Solution {
    public int lengthOfLongestSubstring(String s) {
        Map<Character, Integer> map = new HashMap<>();
        int max = 0;

        for (int l=0, r=0; r<s.length(); r++) {
            char c = s.charAt(r);
            if (map.containsKey(c))
                l = Math.max(l, map.get(c));

            max = Math.max(max, r - l + 1);
            map.put(c, r + 1);
        }

        return max;
    }
}


class Solution2 {
    public int lengthOfLongestSubstring(String s) {
        Set<Character> set = new HashSet<Character>();
        int max = 0;
        int l = 0;
        int r = 0;
        while (r < s.length()) {
            char c = s.charAt(r);

            while (set.contains(c))
                set.remove(s.charAt(l++));

            set.add(c);
            max = Math.max(max, ++r - l);
        }

        return max;
    }
}