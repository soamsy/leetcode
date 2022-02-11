from functools import cache
def canFinish(numCourses: int, prerequisites: list[list[int]]) -> bool:
    graph = {}
    for a, b in prerequisites:
        graph[a] = graph.get(a, []) + [b]
            
    taken = set()
    @cache
    def fn(course):
        if course in taken:
            return False
        
        if not graph.get(course, []):
            return True
        
        taken.add(course)
        possible = all([fn(c) for c in graph[course]])
        taken.remove(course)
        return possible
    
    return all(fn(c) for c in range(numCourses))