class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        q = n
        ternary_num = set()

        while q != 0:
            ternary_num.add(q%3)
            q = q//3

        return False if 2 in ternary_num else True 