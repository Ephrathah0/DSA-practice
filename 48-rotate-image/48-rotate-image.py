class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        m,n = len(matrix),len(matrix[0])
        r,c = 0,0
        dic = {}
        while r<m and c<n:
            a,b = str(r),str(c)
            z = a+":"+b
            dic.update({z:matrix[r][c]})
            if c==n-1:
                r+=1
                c=-1
            c+=1
        r,c=m-1,0
        a,b=0,0
        while r>=0 and c<n:
            p,q = str(r),str(c)
            l = p+":"+q
            z = dic[l]
            matrix[a][b]=z
            if b==n-1:
                a+=1
                b=-1
            b+=1
            if r==0:
                r=m
                c+=1
            r-=1