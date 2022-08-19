class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        cityMap = {} 
        for city1, city2 in paths:
            cityMap[city1] = city2
            
        for city1,city2 in paths:

            if city2 not in cityMap: 
                return city2
        