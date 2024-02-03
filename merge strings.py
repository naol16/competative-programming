class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        length_of_first=len(word1)
        length_of_second=len(word2)
        length_of_min=min(length_of_first,length_of_second)
        newstring=""
        for i in range(0,length_of_min):
            newstring+=word1[i]
            newstring+=word2[i]
        if length_of_first>length_of_second:
            newstring+=word1[length_of_min:length_of_first]
        elif length_of_second>length_of_first:
             newstring+=word2[length_of_min:length_of_second]
        return newstring
             

        
        
