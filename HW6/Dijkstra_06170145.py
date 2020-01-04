from collections import defaultdict
from collections import OrderedDict
#Class to represent a graph
class Graph():

    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [] 
        self.graph_matrix = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
    def addEdge(self,u,v,w): 
        
        self.graph.append([u,v,w])
        
    def Dijkstra(self, s): 
        dist = dict()
        for a in range(self.V):
            dist[str(a)] = float("Inf")
        dist[str(s)] = 0
        
        Queue = [False] * self.V
        
        for cnt in range(self.V):
            u = self.ExtractMin(dist, Queue)
            Queue[u] = True
            for v in range(self.V): #relax
                if self.graph[u][v]>0: #adj[u] edge
                    if Queue[v] == False:
                        if dist[str(v)] > dist[str(u)] + self.graph[u][v]:
                            dist[str(v)] = dist[str(u)] + self.graph[u][v]
        return dist                    
        
    def ExtractMin(self, dist, Queue):
        Min = float("Inf")
        for v in range(self.V):
            if dist[str(v)] < Min and Queue[v] == False:
                Min = dist[str(v)]
                min_index = v
        return min_index



    def Kruskal(self):
        d2={}
        min_arr=[]
        treegraph=[]
        answer=[]
        temp1=0
        temp2=0
        #print(len(self.graph))
        #print (self.V)
        for i in range(len(self.graph)-1):
            for j in range(len(self.graph)-i-1):
                if(self.graph[j][2]>self.graph[j+1][2]):
                    temp=self.graph[j]
                    self.graph[j]=self.graph[j+1]
                    self.graph[j+1]=temp
        #print(self.graph)
        min_arr.append(self.graph[0][0])
        min_arr.append(self.graph[0][1])
        treegraph.append(0)
        for i in range(1,self.V):
            flag1=0
            flag2=0
            for j in range(len(min_arr)):
                if(min_arr[j]==self.graph[i][0]):
                    flag1+=1
                if(min_arr[j]==self.graph[i][1]):
                    flag2+=1
            if((flag1+flag2)!=2):
                if(flag1!=1):
                    min_arr.append(self.graph[i][0])
                if(flag2!=1):
                    min_arr.append(self.graph[i][1])
                treegraph.append(i)
        #print(min_arr)
        #print(treegraph)
        for i in range(len(treegraph)):
            answer.append("'"+str(self.graph[treegraph[i]][0])+"-"+str(self.graph[treegraph[i]][1])+"': "+str(self.graph[treegraph[i]][2]))
            d2[str(str(self.graph[treegraph[i]][0])+"-"+str(self.graph[treegraph[i]][1]))] = self.graph[treegraph[i]][2]
        #print (answer)
        OrderedDict(sorted(d2.items(), key=lambda t: t[1]))
        #print (d2)
        return(d2)



