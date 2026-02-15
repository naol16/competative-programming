class Solution:
    def numTrees(self, n: int) -> int:
        #we are going to define the answer array
        answer=[1 for i in range(n+1)]
        for  nodes in range(2,len(answer)):
             possibleways=0
             for position in range (1,nodes+1):
                 left=position-1
                 right=nodes-position
                 possibleways+=answer[left]*answer[right]
             answer[nodes]=possibleways
        return answer[n]
