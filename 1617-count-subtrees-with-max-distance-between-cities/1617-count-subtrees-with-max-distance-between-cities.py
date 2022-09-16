from collections import defaultdict
class Solution:
    def countSubgraphsForEachDiameter(self, n: int, edges: List[List[int]]) -> List[int]:
        
        graph = [[] for i in range(n + 1)]
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
            
        chosen_ver = set()
        ans_map = defaultdict(int)
        self.all_potential_subtrees(graph, n, chosen_ver, ans_map, 1)
        res = []
        for i in range(1, n):
            if i in ans_map:
                res.append(ans_map[i])
            else:
                res.append(0)
        
        return res
    
    def all_potential_subtrees(self, graph, n, chosen_ver, ans_map, curr):
        if curr > n:
            if chosen_ver:
                vis = set()
                st_ver = next(iter(chosen_ver))
                _, dia = self.find_dia(graph, n, chosen_ver, st_ver, vis)
                if len(vis) == len(chosen_ver):
                    ans_map[dia] += 1
            return
        
        chosen_ver.add(curr)
        self.all_potential_subtrees(graph, n, chosen_ver, ans_map, curr + 1)
        chosen_ver.remove(curr)
        self.all_potential_subtrees(graph, n, chosen_ver, ans_map, curr + 1)
    
    def find_dia(self, graph, n, chosen_ver, curr_ver, vis):
        max1, max2, max_dia = (0, 0, 0)
        vis.add(curr_ver)
        for child in graph[curr_ver]:
            if child in chosen_ver and child not in vis:
                max_edge, dia = self.find_dia(graph, n, chosen_ver, child, vis)
                if max_edge > max1:
                    max2 = max1
                    max1 = max_edge
                elif max_edge > max2:
                    max2 = max_edge
                max_dia = max(max_dia, dia)
        max_dia = max(max1 + max2, max_dia)
        return max(max1 + 1, max2 + 1), max_dia