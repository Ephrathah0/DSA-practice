class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        result= []
        for n in range(1,n+1):            
            if n%3==0 and n%5==0:
                result.append("FizzBuzz")
            elif n%3==0:
                result.append("Fizz")
            elif n%5==0:    
                result.append("Buzz")
            else:
                result.append(str(n))
        return result
                