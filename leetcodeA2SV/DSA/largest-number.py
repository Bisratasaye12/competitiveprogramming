class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        new = list(map(str, nums))

        for i in range(len(nums)):
            for j in range(len(new) -i-1):
                print(new[j] + new[j+1] , new[j+1] + new[j])
                if new[j] + new[j+1] < new[j+1] + new[j]:
                    new[j], new[j+1] = new[j+1], new[j]



        return "0" if int("".join(new)) == 0 else "".join(new)