class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        
        boxTypes.sort(key=lambda x: x[1], reverse=True)

        
        max_units = 0
        
        for num_boxes, units in boxTypes:
            
            to_remove = min(truckSize, num_boxes)
            truckSize -= to_remove
            
            max_units += to_remove * units
            
            if truckSize == 0:
                break
            
        return max_units