from collections import deque
class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        newlist=[0]*len(deck)
        queue=deque(range(len(deck)))
        
        for i in deck:
            num=queue.popleft()
            newlist[num]=i
            if queue:
               queue.append(queue.popleft())
            
            
        
        return newlist
        
        