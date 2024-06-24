class Graph:

    def __init__(self,vno):
        self.vertex_count=vno
        self.adj_list={vno:[] for e in range(vno)}

    def add_edge(self,u,v,weight=1):
        if 0<=u<=self.vertex_count and 0<=v<=self.vertex_count:
            self.adj_list.append((v,weight))
            self.adj_list.append((u,weight))

        else:
            print("invalid request")

    def remove_edge(self,u,v):
        if 0<=u<=self.vertex_count and 0<=v<=self.vertex_count:
            pass        