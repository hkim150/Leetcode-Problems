/**
 * @param {string} s
 * @return {string}
 */
var decodeString = function(s) {
    let decode = function(s, rep) {
        let stack = 0;
        let i = 0;
        let found = false;
        let num_start = 0;
        let par_start = 0;
        let num = 0;
        
        while (i < s.length) {
            if (found) {
                if (s[i] === '[') {
                    stack++;
                    if (par_start === 0) {
                        par_start = i;
                    }
                    if (num === 0) {
                        num = parseInt(s.slice(num_start, i));
                    }
                } else if (s[i] === ']') {
                    stack--;
                    if (stack === 0) {
                        let sub_s = decode(s.slice(par_start+1, i), num);
                        s = s.slice(0, num_start) + sub_s + s.slice(i+1);
                        i += sub_s.length - (i - num_start + 1);
                        found = false;
                        num_start = 0;
                        par_start = 0;
                        num = 0;
                    }
                }
            } else {
                if (!isNaN(parseInt(s[i]))) {
                    found = true;
                    num_start = i;
                }
            }
            
            i++;
        }
        
        return s.repeat(rep);
    }
    
    return decode(s, 1);
};