import sys
class Graph:
    def add_undirected(self, u ,v):
        self.adj[u].append(v)
        self.adj[v].append(u)
    def read(self):
        self.count = 1
        line1 = sys.stdin.readline().split()
        self.n = int(line1[0])
        self.m = int(line1[1])
        self.adj = [[] for i in range(self.n)]
        self.count_list = [ 0 for i in range(self.n)]
        for i in range(self.m):
            line = list(map(int,sys.stdin.readline().split()))
            self.add_undirected(line[0]-1 ,line[1]-1 )
            self.visited = [False for i in range(self.n) ]
    def explore( self , vertex ):
        self.visited[vertex] = True
        self.count_list[vertex] = self.count
        for edge in self.adj[vertex] :
            if self.visited[edge] == False:
                self.explore(edge)
    def DFS(self):
        if self.m >0:

            for i in range(len(self.visited)):
                if self.visited[i] == False:
                    self.explore(i)
                    self.count += 1
        else:
            self.count = self.n +1
    def run(self):
        self.read()
        self.DFS()
        print(self.count - 1 )
Test = Graph()
Test.run()