from collections import defaultdict
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        dictionary=defaultdict(list)
        for i,j in edges:
            dictionary[i].append(j)
            dictionary[j].append(i)
        stack=[source]
        visted=set([source])
        
        while stack:
              element=stack.pop()
              if element==destination:
                 return True
              for i in dictionary[element]:
                  if i not in visted:
                     stack.append(i)
                     visted.add(i)
        return False
                
            