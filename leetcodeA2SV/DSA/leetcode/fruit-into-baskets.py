class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        NUMBER_OF_BASKETS = 2
        hashmap = defaultdict(int)
        l, m = 0,0
        mx = 0
        count = 0
        while m < len(fruits):
           hashmap[fruits[m]] += 1
           count += 1

           while len(hashmap) > NUMBER_OF_BASKETS:
               elem = fruits[l]
               hashmap[elem] -= 1
               count -= 1
               if hashmap[elem] == 0:
                   hashmap.pop(elem)
               l += 1

           mx = max(count, mx)
           m += 1

        return mx

        