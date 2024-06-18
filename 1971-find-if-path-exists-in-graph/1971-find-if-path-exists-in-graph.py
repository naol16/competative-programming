from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dictionary=defaultdict(list)
        for i,j in edges:
            dictionary[i].append(j)
            dictionary[j].append(i)
        visted=set()
        def dfs(source):
            if source==destination:
               return True
            visted.add(source)
            for  i in dictionary[source]:
                 if  i not in visted and dfs(i):
                    return True
            return False
        return dfs(source)
                 