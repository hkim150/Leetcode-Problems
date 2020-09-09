class Solution {
    public List<Integer> findAnagrams(String s, String p) {
        List<Integer> ans = new ArrayList<>();
        if (s.length() == 0 || s.length() < p.length())
            return ans;

        final int num_letters = 26;
        int a_ascii = (int)'a';
        int[] s_count = new int[num_letters];
        int[] p_count = new int[num_letters];

        for (int i=0; i<p.length(); i++) {
            p_count[(int)p.charAt(i) - a_ascii]++;
            s_count[(int)s.charAt(i) - a_ascii]++;
        }

        boolean found;
        for (int i=0; i<s.length()-p.length(); i++) {
            found = true;
            for (int j=0; j<num_letters; j++) {
                if (s_count[j] != p_count[j])
                    found = false;
            }

            if (found)
                ans.add(i);

            s_count[(int)s.charAt(i) - a_ascii]--;
            s_count[(int)s.charAt(i+p.length()) - a_ascii]++;
        }

        found = true;
        for (int j=0; j<num_letters; j++) {
            if (s_count[j] != p_count[j])
                found = false;
        }

        if (found)
            ans.add(s.length()-p.length());

        return ans;
    }
}