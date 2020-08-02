class MinStack {

    private List<Integer> stack;
    private List<Integer> minStack;

    /** initialize your data structure here. */
    public MinStack() {
        this.stack = new ArrayList<Integer>();
        this.minStack = new ArrayList<Integer>();
    }

    public void push(int x) {
        this.stack.add(x);

        if (this.minStack.size() == 0 || x <= this.minStack.get(this.minStack.size()-1)) {
            this.minStack.add(x);
        }
    }

    public void pop() {
        int popNum = this.stack.get(this.stack.size()-1);
        if (popNum == this.minStack.get(this.minStack.size()-1))
            this.minStack.remove(this.minStack.size()-1);

        this.stack.remove(this.stack.size()-1);
    }

    public int top() {
        return this.stack.get(this.stack.size()-1);
    }

    public int getMin() {
        return this.minStack.get(this.minStack.size()-1);
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */