class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        s = set()
        k = 0
        n = 0
        idxs = []
        for i in range(len(nums)):
            if nums[i] in s:
                idxs.append(i)
            else:
                s.add(nums[i])
                k += 1

        modif = 0
        for i in idxs:
            nums.append(nums.pop(i-modif))
            modif += 1
        return k

