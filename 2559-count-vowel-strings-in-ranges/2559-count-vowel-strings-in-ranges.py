class Solution(object):
    def vowelStrings(self, words, queries):
        """
        :type words: List[str]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        vowels = {'a', 'e', 'i', 'o', 'u'}
        prefix_sum = []
        res = []
        cnt = 0
        
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                cnt += 1
            prefix_sum.append(cnt)
        
        for query in queries:
            if query[0] > 0:
                cnt = prefix_sum[query[1]] - prefix_sum[query[0] - 1]
            else:
                cnt = prefix_sum[query[1]]
            res.append(cnt)
        
        return res
        
        