class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        result=True
        n=str(x)
        
        while result is True and len(n)>1:
            if n[0]==n[len(n)-1]:
                n=n[1:len(n)-1]
            else:
                result=False
        return result
        