class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # we can use recursion to exhaustively search all solutions
        # by only going over same or greater candidates than the last one, we can avoid duplicates
        cand = sorted(candidates)
        
        ans = []
        def helper(t, lst=[], idx=0):
            for i in range(idx, len(cand)):
                next_t = t - cand[i]
                if next_t > 0:
                    helper(next_t, lst + [cand[i]], i)
                elif next_t == 0:
                    ans.append(lst + [cand[i]])
                        
        helper(target)
        return ans