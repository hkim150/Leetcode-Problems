/**
 * @param {number} numCourses
 * @param {number[][]} prerequisites
 * @return {boolean}
 */
var canFinish = function(numCourses, prerequisites) {
    let graph = {};
    for (let [dst, src] of prerequisites) {
        if (graph.hasOwnProperty(src)) {
            graph[src].push(dst);
        } else {
            graph[src] = [dst];
        }
    }
    
    let checking = {}
    let checked = {}
    
    let hasCycle = function(src) {
        if (checking.hasOwnProperty(src)) {
            return true;
        }
        
        if (checked.hasOwnProperty(src)) {
            return false;
        }
        
        checking[src] = true;
        
        dst = graph.hasOwnProperty(src) ? graph[src] : [];
        for (let d of dst) {
            if (hasCycle(d)) {
                return true;
            }
        }
        
        delete checking[src];
        checked[src] = true;
        
        return false;
    }
    
    for (let src of Object.keys(graph)) {
        if (hasCycle(src)) {
            return false;
        }
    }
    
    return true;
};