class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # dfs traversal in a dag
        g = {}
        for dst, src in prerequisites:
            if src in g:
                g[src].append(dst)
            else:
                g[src] = [dst]
        
        visited = set()
        visiting = set()
        
        def hasCycle(src):
            if src in visiting:
                return True
            
            if src in visited:
                return False
            
            visiting.add(src)
            
            for dst in g.get(src, []):
                if hasCycle(dst):
                    return True
            
            visiting.remove(src)
            visited.add(src)
            return False
        
        for src in g.keys():
            if hasCycle(src):
                return False
            
        return True