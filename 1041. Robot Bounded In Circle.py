class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        i,j = 0,0
        idx_i,idx_j = 0,1
        for instruction in instructions:
            if instruction == 'G':
                i+=idx_i
                j+=idx_j
            elif instruction == 'L':
                idx_i,idx_j = -1*idx_j,idx_i
            else:
                idx_i,idx_j = idx_j,-1*idx_i
        return (i,j) == (0,0) or (idx_i,idx_j) != (0,1) 
