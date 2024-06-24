class Graph:
    def __init__(self,vno):
        self.vertex_count=vno

        self.adj_mtx=[[0]*vno for e in range(vno)]


    def add_edge(self,u,v,weight=1):
        if 0<=u<=self.vertex_count and 0<=v<=self.vertex_count:

            self.adj_mtx[u][v]=weight
            self.adj_mtx[v][u]=weight

        else:
            print("invalid index ")



    def remove(self,u,v):
        if 0<=u<=self.vertex_count and 0<=v<=self.vertex_count:
            self.adj_mtx[u][v]=0
            self.adj_mtx[v][u]=0

        else:
            print("invalid request")                      



    def has_edge(self,u,v):
        if 0<=u<=self.vertex_count and 0<=v<=self.vertex_count:
            return self.adj_mtx[u][v]!=0
        else:
            print("invalid edge request")



    def iterator(self):
        for row_list in self.adj_mtx:
            print("".join(map(str,row_list)))



#driver code
graph=Graph(5)

graph.add_edge(0,0)
graph.add_edge(0,1)
graph.add_edge(0,2)
graph.add_edge(0,3)
graph.add_edge(0,4)

graph.iterator()


graph.remove(0,3)

graph.has_edge(0,3)

print("after removal")

graph.iterator()

