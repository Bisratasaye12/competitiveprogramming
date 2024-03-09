class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        n = len(nums)
        mn = float('inf')

        stack_queue = deque()
        r = 0

        for i,j in enumerate(nums):
            r += j
            if r >= k: 
                mn = min(mn, i+1)

            while stack_queue and (r - stack_queue[0][0]) >= k:
                elem = stack_queue.popleft()
                mn = min(mn, i - elem[1])

            while stack_queue and stack_queue[-1][0] >= r:
                stack_queue.pop()

            stack_queue.append((r, i))

        return mn if mn != float('inf') else -1




        