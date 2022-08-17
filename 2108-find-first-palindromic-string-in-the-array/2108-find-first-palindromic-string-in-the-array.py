class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        stack=[]
        for i in words:
            if i== i[::-1]:
                stack.append(i)
        if stack:
            return stack[0]
        if len(stack)==0:
            return ""
       #  print(stack) 
            
        