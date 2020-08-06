class Solution {
    public int[] dailyTemperatures(int[] T) {
        Stack<Integer> stack = new Stack<>();
        int[] ans = new int[T.length];

        for (int i=T.length-1; i>-1; i--) {
            while (!stack.empty() && T[stack.peek()] <= T[i])
                stack.pop();

            ans[i] = stack.empty() ? 0 : stack.peek() - i;
            stack.push(i);
        }

        return ans;
    }
}