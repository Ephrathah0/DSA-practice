class Solution:
    def myPow(self, x: float, n: int) -> float:
        def recur(m,n):
            if n==0:
                return 1
            if n==1:
                return m
            else:
                temp=recur(m,n//2)
                if n%2!=0:
                    return temp*temp*m
                else:
                    return temp*temp
        if n<0:
            return (1/recur(x,abs(n)))
        return recur(x,abs(n))