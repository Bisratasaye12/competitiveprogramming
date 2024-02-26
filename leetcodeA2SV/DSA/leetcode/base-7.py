class Solution:
    def convertToBase7(self, num: int) -> str:
        ans = []
        if num == 0: return "0"

        q = abs(num)

        while q > 0:
            r = q%7
            ans.append(r)
            q //= 7


        return "".join(map(str, ans[::-1])) if num >= 0 else "".join(map(str, ["-"] + ans[::-1]))