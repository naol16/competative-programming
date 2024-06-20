
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        listone=[-1 for i in range(len(graph))]
        def dfs(node):
            for nodes in  graph[node]:
                if listone[nodes]!=-1:
                   if listone[node]==listone[nodes]:
                      return False
                else:
                     listone[nodes]=1-listone[node]
                     if  not dfs(nodes):
                         return False
            return True
        for i in range(len(graph)):
            if listone[i]==-1:
               listone[i]=0
               if not dfs(i):
                 return False
        return True