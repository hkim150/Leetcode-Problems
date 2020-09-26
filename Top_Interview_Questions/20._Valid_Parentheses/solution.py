class Solution:
    def isValid(self, s: str) -> bool:
        # we can use stack to push in opening parentheses and
        # compare the poped paren when we encounter a closing paren
        stack = []
        opening = ('[', '{', '(')
        closing = (']', '}', ')')
        match = {closing[i] : opening[i] for i in range(len(opening))}
        
        for p in s:
            if p in opening:
                stack.append(p)

            elif p in closing:
                if len(stack) < 1:
                    return False
                
                last = stack.pop()
                if match[p] != last:
                    return False
            
        return len(stack) == 0