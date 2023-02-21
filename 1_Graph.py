# 1. Write a python program to design & analyze the application of Artificial Intelligence for Graph Theory concept.

graph = { "a" : {"c"},
          "b" : {"c", "e"},
          "c" : {"a", "b", "d", "e"},
          "d" : {"c"},
          "e" : {"c", "b"},
          "f" : {}
        }

def genEdges(graph):
    edges = []   
    for node in graph:
        for neighbor in graph[node]:
            edges.append({node, neighbor})
    return edges

print(genEdges(graph))

def findIsolatedNodes(graph):
    isolated = set()
    for node in graph:
        if not graph[node]:
            isolated.add(node)
    return isolated
class Graph(object):
    def __init__(self, graphDict=None):
        if graphDict == None:
            graphDict = {}
        self._graphDict = graphDict

    def edges(self, vertice):
        return self._graphDict[vertice]
        
    def allVertices(self):
        return set(self._graphDict.keys())

    def allEdges(self):
        return self.__genEdges()

    def addVertex(self, vertex):
        if vertex not in self._graphDict:
            self._graphDict[vertex] = []

    def addEdge(self, edge):
        edge = set(edge)
        vertex1, vertex2 = tuple(edge)
        for x, y in [(vertex1, vertex2), (vertex2, vertex1)]:
            if x in self._graphDict:
                self._graphDict[x].add(y)
            else:
                self._graphDict[x] = [y]

    def __genEdges(self):
        edges = []
        for vertex in self._graphDict:
            for neighbor in self._graphDict[vertex]:
                if {neighbor, vertex} not in edges:
                    edges.append({vertex, neighbor})
        return edges
    
    def __iter__(self):
        self._iterObj = iter(self._graphDict)
        return self._iterObj
    
    def __next__(self):
        return next(self._iterObj)

    def __str__(self):
        res = "Vertices: "
        for k in self._graphDict:
            res += str(k) + " "
        res += "\nEdges: "
        for edge in self.__genEdges():
            res += str(edge) + ""
        return res


g = { "a" : {"d"},
      "b" : {"c"},
      "c" : {"b", "c", "d", "e"},
      "d" : {"a", "c"},
      "e" : {"c"},
      "f" : {}
    }

graph = Graph(g)

for vertice in graph:
    print(f"Edges of vertice {vertice}: ", graph.edges(vertice))