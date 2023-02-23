class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1,x2,x3,x4=rec1[0], rec1[2], rec2[0], rec2[2]
        y1,y2,y3,y4=rec1[1], rec1[3], rec2[1], rec2[3]
        if((x3>x1 and x3<x2)  or  (x4>x1 and x4<x2) or (x1>x3 and x1<x4) or (x2>x3 and x2<x4)):
            if((y3>y1 and y3<y2)  or  (y4>y1 and y4<y2) or (y1>y3 and y1<y4) or (y2>y3 and y2<y4)):
                return True
        
        return False
		
