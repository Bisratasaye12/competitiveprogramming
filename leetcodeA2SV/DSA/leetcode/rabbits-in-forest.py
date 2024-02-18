class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        mnNum = 0

        for ans in count:
            size = ans + 1
            if ans > count[ans]:
                mnNum += size
            elif count[ans] % size == 0:
                mnNum += count[ans]
            else:
                mnNum += (count[ans] // size) * size + size

        return mnNum