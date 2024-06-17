class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        list2=set()
        list1=set()
        answer=[]
        for i,j in edges:
            list2.add(j)
            list1.add(i)
        for i in list1:
            if i not in list2:
               answer.append(i)
            
            
        return answer
            
        