class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        
        l, r = 0, len(nums)-1
        idx = defaultdict(int)
        for i,j in enumerate(nums):
            idx[j] = i

        nums.sort()
        count = 0
        print(nums)

        while l < r:
            s = nums[l] + nums[r]
            i1, i2 = idx[nums[l]], idx[nums[r]]
           
            if s < target:
                count += (r-l)
                l += 1
            else:
                r -= 1
           
                

        return count

     
      


        


            

