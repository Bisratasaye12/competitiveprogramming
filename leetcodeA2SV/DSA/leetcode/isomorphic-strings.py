class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapper = defaultdict(str)
        mapper2 = defaultdict(str)

        for i,j in zip(s,t):
            if i in mapper or j in mapper2:
                if j == mapper[i] or i == mapper[j]: continue
                else:
                    return False
            else:
                mapper[i] = j
                mapper2[j] = i

        print(mapper, mapper2)

        return True
