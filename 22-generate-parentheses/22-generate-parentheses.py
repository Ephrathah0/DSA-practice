class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        opening_bracket = n
        closing_bracket = n
        ans = []

        self.generate_sequence(opening_bracket, closing_bracket, '', ans)
        return ans

    def generate_sequence(self, opening_bracket, closing_bracket, ssf, ans):
        
        if(opening_bracket == 0 and closing_bracket == 0):
            ans.append(ssf)
            return

        if(opening_bracket > 0):
           
            self.generate_sequence(opening_bracket-1, closing_bracket, ssf+'(', ans)
        if(closing_bracket > 0 and closing_bracket > opening_bracket):
           
            self.generate_sequence(opening_bracket, closing_bracket-1, ssf+')', ans)