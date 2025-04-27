import sys
class Graph:
    def add_directed(self, u ,v):
        self.adj[u].append(v)
    def read(self):
        self.count = 1
        self.cycle_check = False
        line1 = sys.stdin.readline().split()
        n = int(line1[0])
        m = int(line1[1])
        self.adj = [[] for i in range(n)]
        self.count_list = [0 for i in range(n)]
        for i in range(m):
            line = list(map(int,sys.stdin.readline().split()))
            self.add_directed(line[0]-1 ,line[1]-1 )
        self.visited = [False for i in range(n) ]
        self.restack = [False for i in range(n) ]
    def explore( self , vertex ):
        self.visited[vertex] = True
        self.restack[vertex] = True
        for edge in self.adj[vertex]:
            if self.visited[edge] == False:
                self.explore(edge)
            if self.restack[edge] == True:
                self.cycle_check = True
            if self.cycle_check:
                break
        self.restack[vertex] = False
    def DFS(self):
        for i in range(len(self.visited)):
            self.restack = [False for i in range(len(self.visited)) ]
            if self.visited[i] == False:
                self.explore(i)
            if self.cycle_check:
                break
    def run(self):
        self.read()
        self.DFS()
        if self.cycle_check:
            print(1)
        else:
            print(0)
Test = Graph()
Test.run()