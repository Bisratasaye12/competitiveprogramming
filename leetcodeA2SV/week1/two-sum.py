class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        item_index = defaultdict(list)
        for i,j in enumerate(nums):
            item_index[j].append(i)

        for i in nums:
            if target - i in item_index:
                u = item_index[i][0]
                v = item_index[target - i][0]
                if u != v:
                    return item_index[i] + item_index[target - i]
                else:
                    if len(item_index[target - i]) > 1:
                        return [item_index[i][0] , item_index[target - i][1]]



        
        



            
            

