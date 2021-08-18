#Page 109 to page 241
class Graph():
    def __init__(self):
        self.graph = {}
    
    def addEdge(self, data, connect):
        if data in self.graph:
            self.graph[data].append(connect)
        else:
            self.graph[data] = [connect]
    
    def route(self, start, end):
        visited = {}
        queue = []
        visited[start] = True
        queue.append(start)
        while queue:
            n = queue.pop(0)
            if n == end:
                return
            for i in self.graph[n]:
                if i not in visited:
                    queue.append(i)
                    visited[i] = True
        return False
g = Graph(4) 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3)
print(g.route(1, 3))
print(g.route(3, 1))