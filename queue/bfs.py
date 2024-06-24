from queue1 import *


class BFS:
    def __init__(self,graph):
        self.graph=graph
        self.q=Queue()


    def bfs(self,start):

        visited={}
        self.q.enqueue(start)

        visited[start]=True

        while not self.q.empty():
            n=self.q.see_front()

            self.q.dequeue()

            print(n)

        for neighbour in self.graph[n]:
            if neighbour not in visited:
                self.q.enqueue(neighbour)
                visited[neighbour]=True

graph = {
    0: [1, 2],
    1: [2],
    2: [0, 3],
    3: [3]
}
bfs_obj=BFS(graph)
bfs_obj.bfs(1)




    
    


    