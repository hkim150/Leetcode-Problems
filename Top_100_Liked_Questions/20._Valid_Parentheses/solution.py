class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        
        # using hash set and hash map for constant time check
        openingParen = set(['(', '{', '['])
        matchingParen = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        
        for paren in s:
            if paren in openingParen:
                stack.append(paren)
            else:
                if not stack or stack.pop() != matchingParen[paren]:
                    return False
        
        return len(stack) == 0