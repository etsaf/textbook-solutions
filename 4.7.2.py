#Page 109 to page 241
#Topological sort through DFS
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

    def sortHelp(self, node, visited, stack):
        visited[node] = True
        for i in self.graph[node]:
            if visited[i] == False:
                self.sortHelp(i, visited, stack)
        stack.insert(0, node)

    def topoSort(self):
        visited = {}
        for i in self.graph:
            visited[i] = False
        stack = []
        for i in self.graph:
            if visited[i] == False:
                self.sortHelp(i, visited, stack)
        return stack