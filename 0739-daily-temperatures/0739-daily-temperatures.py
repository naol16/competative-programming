from collections import defaultdict
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack1=[]
        array=[0]*len(temperatures)
        for i in range(len(temperatures)):
            while stack1 and temperatures[stack1[-1]]<temperatures[i]:
                  array[stack1[-1]]=i-stack1[-1]
                  stack1.pop()
            stack1.append(i)
        return array
        