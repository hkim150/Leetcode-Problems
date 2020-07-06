/**
 * @param {number[]} coins
 * @param {number} amount
 * @return {number}
 */
var coinChange = function(coins, amount) {
    mem = new Array(amount+1).fill(Infinity);
    mem[0] = 0;
    
    for (let coin of coins) {
        for (let i=coin; i<amount+1; i++) {
            mem[i] = Math.min(mem[i], mem[i-coin] + 1);
        }
    }
    
    return mem[amount] != Infinity ? mem[amount] : -1;
};