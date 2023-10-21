class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        res = []
        r = len(arr) -1
        m = 0
        l = 0
        while r >= 0:
            if l > r:
                l = r
            if arr[l] > arr[m]:
                m = l
                l += 1
            elif l == r:
                arr[:m+1] = reversed(arr[:m+1])
                arr[:r+1] = reversed(arr[:r+1])
                res.append(m+1)
                res.append(r+1)
                m = 0
                r -= 1
                l = 0
            else:
                l += 1

        return res
