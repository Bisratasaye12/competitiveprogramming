class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos, neg = [], []

        for i in nums:
            if i < 0:
                neg.append(i)
            elif i > 0:
                pos.append(i)

        j = 0
        for i in range(0,len(nums),2):
            nums[i] = pos[j]
            nums[i+1] = neg[j]
            j+=1


        return nums