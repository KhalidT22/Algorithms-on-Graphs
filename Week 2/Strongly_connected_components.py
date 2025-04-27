import sys
sys.setrecursionlimit(10**6)

class Graph:
    def add_directed(self, u ,v):
        self.adj[u].append(v)
        self.rev_adj[v].append(u)
    def read(self):
        self.vis_check = False
        line1 = sys.stdin.readline().split()
        self.n = int(line1[0])
        self.m = int(line1[1])
        self.adj = [[] for i in range(self.n)]
        self.rev_adj = [[] for i in range(self.n)]
        self.stack =  []
        self.scc_count = 0
        for i in range(self.m):
            line = list(map(int,sys.stdin.readline().split()))
            self.add_directed(line[0]-1 ,line[1]-1 )
        self.visited = [False for i in range(self.n) ]

    def explore( self , vertex ):
        self.visited[vertex] = True
        for edge in self.adj[vertex]:
            if self.visited[edge] == False:
                self.explore(edge)
        self.stack.append(vertex)

    def rev_explore( self , vertex ):
        #self.comp.append(vertex)
        self.visited[vertex] = True
        for edge in self.rev_adj[vertex]:
            if self.visited[edge] == False:
                self.rev_explore(edge)


    def DFS(self):
        for i in range(len(self.visited)):
            if self.visited[i] == False:
                self.explore(i)

    def rev_DFS(self):
        #print(self.stack)

        self.visited = [False for i in range(self.n)]
        while(len(self.stack)>0):
            #self.comp = []
            vertex = self.stack.pop()
            if self.visited[vertex] == False:
                self.rev_explore(vertex)
                #print(self.comp)
                self.scc_count += 1

    def run(self):
        self.read()
        self.DFS()
        self.rev_DFS()
        print(self.scc_count)

Test = Graph()
Test.run()