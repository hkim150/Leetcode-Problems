class Solution {
    public int numSquares(int n) {
        int[] mem = new int[n+1];
        List<Integer> squares = new ArrayList<>();

        for (int i=2; ; i++) {
            int square = i * i;
            if (square > n)
                break;

            squares.add(square);
            mem[square] = 1;
        }

        for (int i=1; i<=n; i++) {
            if (mem[i] == 1)
                continue;

            mem[i] = mem[i-1];
            for (int j=0; j<squares.size(); j++) {
                if (squares.get(j) >= i-1)
                    break;

                mem[i] = Math.min(mem[i], mem[i - squares.get(j)]);
            }

            mem[i]++;
        }

        return mem[n];
    }
}

class Solution2 {
    public int numSquares(int n) {
        List<Integer> squares = new ArrayList<>();

        int num = 1;
        while (true) {
            int square = num * num;
            if (square == n)
                return 1;
            else if (square < n)
                squares.add(square);
            else
                break;

            num++;
        }

        int min = Integer.MAX_VALUE;
        for (int i=squares.size()-1; i>-1; i--) {
            min = Math.min(min, this.numSquares(n - squares.get(i)));
        }

        return 1 + min;
    }
}