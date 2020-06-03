/**
 * @param {character[]} tasks
 * @param {number} n
 * @return {number}
 */
var leastInterval = function(tasks, n) {
    let arr = new Array(26);
    for (let i=0; i<26; i++) {
        arr[i] = new Array(2).fill(0);
    }
    
    a_ascii = 'A'.charCodeAt(0);
    for (let task of tasks) {
        arr[task.charCodeAt(0) - a_ascii][0] += 1;
    }
    
    let rem_task = tasks.length;
    let itvl = 0;
    
    while (rem_task) {
        // get non-cooldown task with max number of remaining
        let max_cnt = 0;
        let max_task = null;
        let earliest_itvl = itvl + n;
        for (let i=0; i<26; i++) {
            let [cnt, er_itvl] = arr[i];
            if ((er_itvl <= itvl) && (cnt > max_cnt)) {
                max_cnt = cnt;
                max_task = i;
            }
            if (cnt) {
                earliest_itvl = Math.min(earliest_itvl, er_itvl);
            }
        }
        
        if (max_task != null) {
            arr[max_task][0]--;
            arr[max_task][1] = itvl + n + 1;
            rem_task--;
        }
        
        itvl = Math.max(itvl + 1, earliest_itvl);
    }
    
    return itvl;
};