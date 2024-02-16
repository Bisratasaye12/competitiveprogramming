class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        count = Counter(arr)
        arr.sort(key= lambda x: (count[x], x))
        
        r = set(arr[k:])
        
        return len(r)