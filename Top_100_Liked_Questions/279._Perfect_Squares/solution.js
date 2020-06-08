/**
 * @param {number} n
 * @return {number}
 */
var numSquares = function(n) {
    // iterative dp
    let mem = new Array(n+1).fill(Infinity);
    mem[0] = 0;
    
    let num = 1;
    let sqr = 1;
    let squares = [];
    while (sqr <= n) {
        mem[sqr] = 1;
        squares.push(sqr);
        num += 1;
        sqr = num * num;
    }

    for (let i=2; i<n+1; i++) {
        if (mem[i] == 1) {
            continue
        }
        for (let sqr of squares) {
            if (sqr > i) {
                break;
            }
            mem[i] = Math.min(mem[i], 1 + mem[i - sqr]);
        }
    }

    return mem[n];
}

var numSquares2 = function(n) {
    // recursive dp
    let num = 1;
    let sqr = 1;
    let squares = {};
    
    while (sqr <= n) {
        squares[sqr] = sqr;
        num += 1;
        sqr = num * num;
    }
    
    let helper = function(n) {
        if (n == 0) {
            return 0;
        }

        if (squares.hasOwnProperty(n)) {
            return 1;
        }

        let minNumSquares = Infinity;
        for (let sqr of Object.values(squares).reverse()) {
            if (sqr > n) {
                continue;
            }
            minNumSquares = Math.min(minNumSquares, 1 + helper(n - sqr));
        }
        return minNumSquares;
    }
    
    return helper(n);
};