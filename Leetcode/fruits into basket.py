class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        NUMBER_OF_BASKETS = 2
        hashmap = defaultdict(int)
        l,m = 0,0
        mx = float('-inf')
        idx = 0
        while m < len(fruits):

            if len(hashmap) < NUMBER_OF_BASKETS:
                hashmap[fruits[m]] += 1
                m += 1
                idx = m
                #print("if--", hashmap)
            elif len(hashmap) == NUMBER_OF_BASKETS:
                en = fruits[m]
                if en in hashmap:
                    hashmap[en] += 1
                    m += 1
                    #print("elif-if", hashmap)
                else:
                    #print("elif-else", hashmap)
                    s = sum(hashmap.values())
                    if mx < s:
                        mx = s
                    l = m = idx-1
                    hashmap.clear()
                    #print(idx,mx)
                    
                    
        s = sum(hashmap.values())
        if s > mx:
            mx = s

        return mx

                    




