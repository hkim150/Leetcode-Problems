class Solution {
    public boolean wordBreak(String s, List<String> wordDict) {
        Set<String> set = new HashSet<>(wordDict);
        boolean[] mem = new boolean[s.length()+1];
        mem[0] = true;

        for (int i=1; i<mem.length; i++) {
            for (int j=0; j<i; j++) {
                if (mem[j] && set.contains(s.substring(j, i)))
                    mem[i] = true;
            }
        }

        return mem[s.length()];
    }
}

class Solution2 {
    public boolean wordBreak(String s, List<String> wordDict) {
        Collections.sort(wordDict, (a, b) -> b.length() - a.length());
        return helper(s, wordDict);
    }

    public boolean helper(String s, List<String> wordDict) {
        if (s.length() == 0)
            return true;

        for (String str : wordDict) {
            if (s.startsWith(str) && helper(s.substring(str.length()), wordDict))
                return true;
        }

        return false;
    }
}