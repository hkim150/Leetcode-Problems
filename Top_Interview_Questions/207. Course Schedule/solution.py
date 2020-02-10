class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites:
            return True
        
        # store the prerequisite relationship in hash map
        graph = {}
        unvisited = set()
        
        for dst, src in prerequisites:
            if src in graph:
                graph[src].append(dst)
            else:
                graph[src] = [dst]
            
            unvisited.add(src)
            unvisited.add(dst)
        
        visiting = set()
        visited = set()
        parent = {}
        
        currNode = unvisited.pop()
        
        # check for a cycle while doing DFS traverse
        while True:
            if currNode in visiting:
                return False

            if currNode in visited or currNode not in graph:
                if currNode in parent:
                    parentNode = parent[currNode]
                    del parent[currNode]
                    visiting.remove(parentNode)
                    visited.add(currNode)
                    currNode = parentNode
                    continue
                else:
                    if unvisited:
                        currNode = unvisited.pop()
                    else:
                        return True

            if currNode in graph:
                child = graph[currNode].pop()
                if not graph[currNode]:
                    del graph[currNode]

                parent[child] = currNode
                visiting.add(currNode)
                currNode = child