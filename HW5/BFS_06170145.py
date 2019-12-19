#!/usr/bin/env python
# coding: utf-8

# In[16]:


from collections import defaultdict 
class Graph:
    def __init__(self): 
       
        self.graph = defaultdict(list) 

    
    def addEdge(self,u,v): 
        self.graph[u].append(v) 
  
     
    def BFS(self, s):
        ans=[]
        if s in self.graph:    
            repeated=defaultdict(list)
            queue = [s]
            repeated[s]=True
            while queue:
                vertex=queue.pop(0)
                ans.append(vertex)
                for i in self.graph[vertex]:
                    if not repeated[i]:   
                        repeated[i]=True
                        queue.append(i)
        return ans
    def DFS(self, s):
        path_d=[]
        d=defaultdict(list)
        if s in self.graph:
            stack=[s]
            d[s]='*'
            while(len(path_d)!=len(self.graph)):
                    if not stack: 
                        break
                    vertex=stack.pop()
                    path_d.append(vertex)
                    for i in self.graph[vertex]:
                        if d[i] is not '*': 
                            d[i]='*'
                            stack.append(i)
        else:
            print("the vertex didn't in the graph")
        return path_d          
            
        
    
        


g=Graph()
g.addEdge("A","B")
g.addEdge("A","D")
g.addEdge("B","C")
g.addEdge("B","F")
g.addEdge("C","E")
g.addEdge("C","G")
g.addEdge("D","F")
g.addEdge("E","B")
g.addEdge("E","F")
g.addEdge("F","A")
g.addEdge("G","E")
print(g.BFS("G"))
print(g.DFS("G"))










