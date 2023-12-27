class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
       
       elements = defaultdict(int)
       c = sorted(nums)
       res = []
       for i in range(len(nums)):
           if c[i] not in elements:
               elements[c[i]] = i


       for i in nums:
           res.append(elements[i])
       return res
