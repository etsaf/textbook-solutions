#Page 109 to page 241
#Kahn's algorithm for topological sort
class Graph():
    def __init__(self, n):
        self.graph = {}
        self.vertices = n
    
    def addEdge(self, data, connect):
        if data in self.graph:
            self.graph[data].append(connect)
        else:
            self.graph[data] = [connect]
        if connect not in self.graph:
            self.graph[connect] = []            
    
    def topoSort(self):
        ancestors = {}
        for i in self.graph:
            if i not in ancestors:
                ancestors[i] = 0
            for j in self.graph[i]:
                if j in ancestors:
                    ancestors[j] += 1
                else:
                    ancestors[j] = 1
        queue = []
        for i in ancestors:
            if ancestors[i] == 0:
                queue.append(i)
        visited = 0
        res = []
        while queue:
            x = queue.pop(0)
            res.append(x)
            visited += 1
            for i in self.graph[x]:
                ancestors[i] -= 1
                if ancestors[i] == 0:
                    queue.append(i)
        if visited != self.vertices:
            return "Err: cycle"
        return res