class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        res = []
        vis = [False] * len(arr1)
        s = []
        for i in range(len(arr2)):
            for j in range(len(arr1)):
                if arr2[i] == arr1[j]:
                    res.append(arr1[j])
                    vis[j] = True
        for i in range(len(arr1)):
            if not vis[i]:
                s.append(arr1[i])
        s = sorted(s)
        return res + s
                    