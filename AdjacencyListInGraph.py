class Graph:
    def __init__(self):
        self.graph={}
        self.directed=False
    def addVertex(self,vertex):
        if vertex not in self.graph:
            self.graph[vertex]=[]

    def addEdge(self,src,dest):
        
        self.addVertex(src)
        self.addVertex(dest)

        self.graph[src].append(dest)
        if not self.directed:
            self.graph[dest].append(src)
    def displaygraph(self):
        for vertex in self.graph:
            print(f"{vertex} ->{self.graph[vertex]}")



    

G=Graph()
G.addEdge('A','B')
G.addEdge('A','D')
G.addEdge('A','C')
G.addEdge('C','D')
G.addEdge('D','E')
G.displaygraph()
