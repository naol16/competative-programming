class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        dictionary={ }
        left=0
        minimumvalue=float('inf')
        for i in range(len(cards)):
            value=cards[i]
            if value in dictionary:
               minimumvalue=min(minimumvalue,i-dictionary[value]+1)
               dictionary[value]=i
        if minimumvalue==float('inf'):
           return -1   
        return minimumvalue
