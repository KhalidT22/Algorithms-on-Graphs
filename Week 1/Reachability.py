import sys
class Graph:
    def add_undirected(self, u ,v):
        self.adj[u].append(v)
        self.adj[v].append(u)
    def read(self):
        line1 = sys.stdin.readline().split()
        n = int(line1[0])
        m = int(line1[1])
        self.adj = [[] for i in range(n)]
        for i in range(m):
            line = list(map(int,sys.stdin.readline().split()))
            self.add_undirected(line[0]-1 ,line[1]-1 )
        self.visited = [False for i in range(n) ]

        line = list(map(int,sys.stdin.readline().split()))
        self.u = line[0]-1
        self.v = line[1]-1
    def explore( self , vertex ):
        self.visited[vertex] = True
        for edge in self.adj[vertex]:
            if self.visited[edge] == False:
                self.explore(edge)
    def run(self):
        self.read()
        self.explore(self.u)
        if self.visited[self.v] == True:
            print(1)
        else:
            print(0)
Test = Graph()
Test.run()