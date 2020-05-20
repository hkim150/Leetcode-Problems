class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # add closing paren only if current comb has fewer closing than opening
        ans = []
        def helper(s='', opening=0, closing=0):
            if len(s) == 2*n:
                ans.append(s)
                return
            
            if opening < n:
                helper(s+'(', opening+1, closing)
            if closing < opening:
                helper(s+')', opening, closing+1)
            
        helper()
        return ans
    
    
    def generateParenthesis2(self, n: int) -> List[str]:        
        # recursive method using a stack
        ans = [] 
        def helper(stack=[], comb="", remOpen=n, remClose=n):
            if remOpen == 0 and remClose == 0:
                ans.append(comb)
                return
            
            if not stack:
                # if stack is empty, we can only push opening paren
                helper(stack + ['('], comb + '(', remOpen-1, remClose)
            else:
                # else, we can push the remaining parens
                if remOpen > 0:
                    helper(stack + ['('], comb + '(', remOpen-1, remClose)
                
                helper(stack[:-1], comb + ')', remOpen, remClose-1)
        
        helper()
        
        return ans