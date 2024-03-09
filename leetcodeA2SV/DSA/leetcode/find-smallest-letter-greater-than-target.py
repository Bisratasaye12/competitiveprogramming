class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        
        mn = chr(123)
        n = len(letters)

        l,r = 0, n-1

        while l <= r:
            mid = (l+r)//2

            if letters[mid] > target:
                mn = min(mn, letters[mid])
                r = mid - 1
            else:
                l = mid + 1  

        return mn if mn != chr(123) else letters[0]