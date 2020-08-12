class Solution {
    public List<String> parens;

    public List<String> generateParenthesis(int n) {
        this.parens = new ArrayList<>();
        this.helper("", n, n);
        return this.parens;
    }

    public void helper(String paren, int open, int close) {
        if (open == 0 && close == 0) {
            this.parens.add(paren);
            return;
        }

        if (open > 0)
            this.helper(paren + "(", open-1, close);

        if (close > open)
            this.helper(paren + ")", open, close-1);
    }
}