class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less, equal, greater = [],[],[]

        for i in nums:
            if i < pivot:
                less.append(i)
            elif i == pivot:
                equal.append(i)
            else:
                greater.append(i)

        less += equal
        
        for i in range(len(less)):
            nums[i] = less[i]

        print(less, greater)
        h = 0
        for i in range(len(less), len(nums)):
            nums[i] = greater[h]
            h += 1

        return nums