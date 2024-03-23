from collections import defaultdict
class Solution(object):
    def longestBeautifulSubstring(self, word):
        """
        :type word: str
        :rtype: int
        """
        dictionary=defaultdict(int)
        length=len(word)
        left=0
        maximum_length=0
        length_word=0
        dictionary[word[0]]=1
        for right in range(1,length):
            if ord(word[right])>=ord(word[right-1]):
               dictionary[word[right]]+=1
            else:
                 dictionary.clear()
                 dictionary[word[right]] += 1
                 left=right
                 
            if len(dictionary)==5:
               length_word=right+1-left
               maximum_length=max(maximum_length,length_word)
        return maximum_length
            
            
                       
                        
                       
            
        
            