class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0:
            return []
        first_num = num//3 - 1
        return [first_num, first_num + 1, first_num + 2]