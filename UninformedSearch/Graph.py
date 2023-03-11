class Graph:
    def __init__(self,Nodes):
        self.nodes = Nodes
        self.graph = {}
        for node in self.nodes:
            self.graph[node] = []
        
    def addEdge(self,V1,V2,e):
        self.graph[V1].append([V2,e])
        self.graph[V2].append([V1,e])

    def addVertex(self,V):
        if V in self.graph:
            pass
        else:
            self.graph[V]=[]
    
    def printGraph(self):
        for node in self.nodes:
            print(node,'->',self.graph[node])



if __name__ == '__main__':
    nodes = ["A","B","C","D",'E']
    G = Graph(nodes)
    G.addEdge('A','B',3)
    G.addEdge('A','C',1)
    G.addEdge('A','D',2)
    G.addEdge('C','B',4)
    G.addEdge('D','B',5)
    G.addEdge('A','E',7)
    G.printGraph()