class Solution {
    public List<String> letterCombinations(String digits) {
        if (digits.length() == 0)
            return new ArrayList<>();

        Map<Character, List<Character>> num2char = new HashMap<>();
        num2char.put('2', new ArrayList<Character>(List.of('a', 'b', 'c')));
        num2char.put('3', new ArrayList<Character>(List.of('d', 'e', 'f')));
        num2char.put('4', new ArrayList<Character>(List.of('g', 'h', 'i')));
        num2char.put('5', new ArrayList<Character>(List.of('j', 'k', 'l')));
        num2char.put('6', new ArrayList<Character>(List.of('m', 'n', 'o')));
        num2char.put('7', new ArrayList<Character>(List.of('p', 'q', 'r', 's')));
        num2char.put('8', new ArrayList<Character>(List.of('t', 'u', 'v')));
        num2char.put('9', new ArrayList<Character>(List.of('w', 'x', 'y', 'z')));

        List<String> ans = new ArrayList<>();
        ans.add("");
        for (int i=0; i<digits.length(); i++) {
            List<Character> chars = num2char.get(digits.charAt(i));
            List<String> currAns = new ArrayList<>(ans);
            ans.clear();
            for (Character ch : chars) {
                for (String s : currAns) {
                    ans.add(s + ch);
                }
            }
        }

        return ans;
    }
}