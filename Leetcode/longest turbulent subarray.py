class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        l, r = 0,1
        ans, prev = 1, ""

        while r < len(arr):

            if arr[r-1] > arr[r] and prev != ">":
                ans = max(ans, r-l+1)
                r += 1
                prev = ">"
            elif arr[r-1] < arr[r] and prev != "<":
                ans = max(ans, r-l+1)
                r += 1
                prev = "<"
            else:
                if arr[r-1] == arr[r]:
                    r += 1
                l = r - 1
                prev = ""

        return ans
