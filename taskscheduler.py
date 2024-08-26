class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)
        ans = 0
        max_heap = []
        for v in freq.values():
            heappush(max_heap,-v)

        time = 0
        q = deque()
        while max_heap or q:
            time+=1
            if max_heap:
                cnt = 1 + heappop(max_heap)
                if cnt:
                    q.append([cnt,time+n])
            if q and q[0][1] == time:
                heappush(max_heap,q.popleft()[0])
        return time
        
