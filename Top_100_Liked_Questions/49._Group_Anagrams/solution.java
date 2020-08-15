class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> hashmap = new HashMap<>();
        int a_ascii = (int) 'a';

        for (String s: strs) {
            int[] count = new int[26];
            for (int i=0; i<s.length(); i++) {
                count[(int) s.charAt(i) - a_ascii]++;
            }

            String key = Arrays.toString(count);
            if (hashmap.containsKey(key))
                hashmap.get(key).add(s);
            else
                hashmap.put(key, new ArrayList<String>(){{add(s);}});
        }

        List<List<String>> ans = new ArrayList<>();
        for (List<String> list : hashmap.values()) {
            ans.add(list);
        }

        return ans;
    }
}


class Solution2 {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> hashmap = new HashMap<>();

        for (String s : strs) {
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String sorted_s = new String(chars);

            if (hashmap.containsKey(sorted_s))
                hashmap.get(sorted_s).add(s);
            else
                hashmap.put(sorted_s, new ArrayList<String>(){{add(s);}});
        }

        List<List<String>> ans = new ArrayList<>();
        for (List<String> list : hashmap.values()) {
            ans.add(list);
        }

        return ans;
    }
}