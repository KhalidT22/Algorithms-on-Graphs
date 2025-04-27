import sys
class Graph:
    def add_directed(self, u ,v):
        self.adj[u].append(v)
    def read(self):
        self.vis_check = False
        line1 = sys.stdin.readline().split()
        self.n = int(line1[0])
        self.m = int(line1[1])
        self.adj = [[] for i in range(self.n)]
        self.top_sort = []
        for i in range(self.m):
            line = list(map(int,sys.stdin.readline().split()))
            self.add_directed(line[0]-1 ,line[1]-1 )
        self.visited = [False for i in range(self.n) ]

    def explore( self , vertex ):

        self.visited[vertex] = True
        self.vis_check = False
        if self.adj[vertex]:
            for edge in self.adj[vertex]:
                if self.visited[edge] == False:
                    self.vis_check = True
                    self.explore(edge)
            if self.vis_check == False:
                self.top_sort.append(vertex)
        else:
            self.top_sort.append(vertex)



    def DFS(self):
        for i in range(len(self.visited)):
            if self.visited[i] == False:
                self.explore(i)
                if self.vis_check:
                    self.top_sort.append(i)
    def Rev_Top(self):
        self.res_top_sort = []
        for i in range(len(self.top_sort)-1,-1,-1):

            self.res_top_sort.append(str(self.top_sort[i]+1))
    def run(self):
        self.read()
        self.DFS()
        self.Rev_Top()

        print(" ".join(self.res_top_sort))

Test = Graph()
Test.run()