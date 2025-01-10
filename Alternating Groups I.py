class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        index=0
        output=0
        while index<len(colors):
              prev,next=index-1,index+1
              if index+1==len(colors):
                 next=0
        
              if colors[index-1]!=colors[index]:
                 if colors[index]!=colors[next]:
                         output+=1
               
              index+=1
        return output
                        
