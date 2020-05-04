/**
 * @param {number[]} prices
 * @return {number}
 */
var maxProfit = function(prices) {
    let maxProf = 0
    let minPrice = Infinity;
    
    prices.forEach(price => {
        if (price < minPrice) {
            minPrice = price;
        } else {
            const profit = price - minPrice;
            if (profit > maxProf) {
                maxProf = profit;
            }
        }
    });
    
    return maxProf;
};