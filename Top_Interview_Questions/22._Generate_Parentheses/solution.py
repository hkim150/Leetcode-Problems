class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # iterative version based on the recursive method below
        gen_paren = []
        queue = [("", n, n)]

        while queue:
            string, opening_left, closing_left = queue.pop(0)
            if opening_left <= 0 and closing_left <= 0:
                gen_paren.append(string)
                continue
            
            if opening_left > 0:
                queue.append( (string + "(", opening_left - 1, closing_left) )
            
            if closing_left > opening_left:
                queue.append( (string + ")", opening_left, closing_left - 1) )
        
        return gen_paren
            
            
    def generateParenthesis2(self, n: int) -> List[str]:
        self.n = n
        self.generated_parentheses = []
        
        self.genParenHelper("", n, n)
        
        return self.generated_parentheses
        
    
    def genParenHelper(self, string, remaining_opening, remaining_closing):
        # if it is complete append it to the list and return
        if remaining_opening <= 0 and remaining_closing <= 0:
            self.generated_parentheses.append(string)
            return
        
        # if there is opening left, recurse on opening paren
        if remaining_opening > 0:
            self.genParenHelper(string + "(", remaining_opening - 1, remaining_closing)
        
        # if the number of closing left is more than that of opening, recurse on the closing paren
        if remaining_closing > remaining_opening:
            self.genParenHelper(string + ")", remaining_opening, remaining_closing - 1)