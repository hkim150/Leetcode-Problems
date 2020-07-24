/**
 * @param {string} secret
 * @param {string} guess
 * @return {string}
 */
var getHint = function(secret, guess) {
    // count bulls
    let bull = 0;
    let c1 = {};
    let c2 = {};
    for (let i=0; i<secret.length; i++) {
        c1[secret[i]] = c1.hasOwnProperty(secret[i]) ? c1[secret[i]] + 1 : 1;
        c2[guess[i]] = c2.hasOwnProperty(guess[i]) ? c2[guess[i]] + 1 : 1;
        if (secret[i] === guess[i]) {
            bull += 1;
        }
    }
    
    // count cows, then cows -= bulls
    let cow = 0;
    for (k of Object.keys(c1)) {
        if (c2.hasOwnProperty(k)) {
            cow += Math.min(c1[k], c2[k]);
        }
    }
    cow -= bull;
    
    return bull.toString() + 'A' + cow.toString() + 'B';
};