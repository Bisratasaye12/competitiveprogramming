class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        queue = deque(timeSeries)
        count = 0

        while queue:
            curr = queue.popleft()
            end = curr + duration 
            #print(curr, end, "ce")

            if queue:
                #print(queue[0], end)
                if queue[0] <= end:
                    count += (queue[0] - curr )
                    continue

            count += duration


        return count
