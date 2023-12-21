class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counts = defaultdict(int)
        
        for i in arr:
            counts[i] += 1


        twenty_five_percent = len(arr)//4

        for i in counts:
            if counts[i] > twenty_five_percent:
                return i

        