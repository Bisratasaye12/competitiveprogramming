class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        queue = deque(enumerate(tickets))
        count = 0
        print(queue[0][0])
        
        i = 0
        while True:
            idx, cur = queue.popleft()
                        
            if cur > 0:
                count += 1
                cur -= 1
                queue.append((idx, cur))
            if idx == k and cur == 0:
                break
            #print(queue)

        return count




