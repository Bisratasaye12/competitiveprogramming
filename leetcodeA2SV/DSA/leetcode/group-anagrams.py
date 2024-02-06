class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

       d = defaultdict(list)
       nw = []
       for i,j in enumerate(strs):
           nw.append((i, "".join(sorted(j))))

       for j,k in nw:
            d[k].append(j)

       res = []
       for i in d:
           t = []
           for j in d[i]:
               t.append(strs[j])
           res.append(t)
           
       return res

