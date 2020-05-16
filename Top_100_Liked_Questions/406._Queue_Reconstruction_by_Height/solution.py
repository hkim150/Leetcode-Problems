class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        # first order by the height in decending order
        # then by the number of people it sees in ascending order
        # finally, insert the elements at index of number of people it sees
        ans = []
        for p in sorted(people, key=lambda x: (-x[0], x[1])):
            ans.insert(p[1], p)
        
        return ans