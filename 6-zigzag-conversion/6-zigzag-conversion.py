class Solution(object):
    def convert(self, s, numRows):
        
        zigzag_list = ["" for i in range(numRows)]
        i = 0
        len_s = len(s)
        
        while i<len_s:
            for j in range(numRows):
                if i<len_s:
                    zigzag_list[j] += s[i]
                    i+=1
            for j in range(numRows-2,0,-1):
                if i<len_s:
                    zigzag_list[j] += s[i]
                    i +=1
                    
        return "".join(zigzag_list)