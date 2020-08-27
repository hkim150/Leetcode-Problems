class Solution {
    public String decodeString(String s) {
        int i=0;
        Stack<Pair> stack = new Stack<>();

        // loop through the string
        while (i < s.length()) {
            // if it sees a number, parse the number n, remove the number and bracket from the string, and push n and the index i_start into the stack
            if (Character.isDigit(s.charAt(i))) {
                // parse the number
                int j = i+1;
                while (Character.isDigit(s.charAt(j))) {
                    j++;
                }
                stack.push(new Pair(i, Integer.parseInt(s.substring(i,j))));
                s = s.substring(0,i) + s.substring(j+1);
            }
            // if it sees a closing bracket at i_end, replace the string from i_start to i_end with the n multiplied string
            else if(s.charAt(i) == ']') {
                Pair p = stack.pop();
                String repeatStr = s.substring(p.index, i);
                String repeatedStr = String.join("", Collections.nCopies(p.mul, repeatStr));
                s = s.substring(0,p.index) + repeatedStr + s.substring(i+1);
                i += repeatedStr.length() - repeatStr.length();
            } else {
                i++;
            }
        }

        return s;
    }
}

class Pair {
    int index;
    int mul;

    public Pair(int index, int mul) {
        this.index = index;
        this.mul = mul;
    }

    @Override
    public String toString() {
        return "(idx: " + this.index + ", mul: " + this.mul + ")";
    }
}