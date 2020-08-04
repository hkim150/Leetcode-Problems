class Solution {
    public boolean isValid(String s) {
        List<Character> stack = new ArrayList<>();
        HashSet<Character> open = new HashSet<>();
        open.add('(');
        open.add('{');
        open.add('[');

        HashMap<Character, Character> hashMap = new HashMap<>();
        hashMap.put(')', '(');
        hashMap.put(']', '[');
        hashMap.put('}', '{');

        for (int i=0; i<s.length(); i++) {
            char ch = s.charAt(i);
            if (open.contains(ch))
                stack.add(ch);
            else {
                if (stack.isEmpty())
                    return false;

                if (!hashMap.get(ch).equals(stack.remove(stack.size()-1)))
                    return false;
            }
        }

        return stack.isEmpty();
    }
}