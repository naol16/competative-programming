class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        dictionary={}
        max_length=0
        length=len(fruits)
        left=0
        for  right in range(length):
             if fruits[right] in dictionary:
                dictionary[fruits[right]]+=1
             else:
                   dictionary[fruits[right]]=1
             while len(dictionary)>2 and left<right :
                   if dictionary[fruits[left]]>1:
                      dictionary[fruits[left]]-=1
                   else:
                        del dictionary[fruits[left]]
                   left+=1
             max_length=max(max_length,right+1-left)
        return max_length
                
                
                
                