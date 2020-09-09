class Solution {
    public Set<Integer> visited;
    public Set<Integer> visiting;
    public Map<Integer, List<Integer>> map;

    public boolean canFinish(int numCourses, int[][] prerequisites) {
        this.map = new HashMap<Integer, List<Integer>>();
        for (int[] prerequisite : prerequisites) {
            List<Integer> prereqs = map.getOrDefault(prerequisite[0], new ArrayList<Integer>());
            prereqs.add(prerequisite[1]);
            map.put(prerequisite[0], prereqs);
        }

        this.visited = new HashSet<Integer>();
        this.visiting = new HashSet<Integer>();
        while (this.map.size() > 0) {
            for (int course : this.map.keySet()) {
                if (!this.dfs(course))
                    return false;

                break;
            }
        }

        return true;
    }

    public boolean dfs(int course) {
        if (this.visited.contains(course))
            return true;

        if (this.visiting.contains(course))
            return false;

        if (this.map.containsKey(course)) {
            this.visiting.add(course);
            List<Integer> prereqs = this.map.get(course);
            for (int i=0; i<prereqs.size(); i++) {
                if (!this.dfs(prereqs.get(i)))
                    return false;
            }
            this.visiting.remove(course);
        }

        this.visited.add(course);
        this.map.remove(course);

        return true;
    }
}