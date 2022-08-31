class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
      
        visited = [0] * numCourses
        graph = defaultdict(list)
        for courses in prerequisites:
            graph[courses[1]].append(courses[0])
            visited[courses[0]] += 1
            
        queue = deque()
        for i in range(numCourses):
            if visited[i] == 0:
                queue.append(i)
        
        course_order = []
        while queue:
            course = queue.popleft()
            course_order.append(course)
            for prerequisite in graph[course]:
                visited[prerequisite] -= 1
                if visited[prerequisite] == 0:
                    queue.append(prerequisite)
                    
        return course_order if len(course_order) == numCourses else []
        