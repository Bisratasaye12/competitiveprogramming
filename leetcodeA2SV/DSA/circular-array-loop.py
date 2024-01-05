class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        n = len(nums)
        

        for i in range(n):
            visited = set()
            j = i
            itself = False
            while j not in visited:
                step = nums[j]
                dest = (j + step) % n
                if (step < 0 and nums[dest] > 0) or (step > 0 and nums[dest] < 0):
                    itself = True
                    break
                if dest == j:
                    itself = True
                    break
                visited.add(j)
                j = dest

            if not itself and visited:
                return True

        return False





