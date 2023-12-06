class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        commons = defaultdict(int)
        sums = defaultdict(list)
        for i in list1:
            commons[i] += 1
        for j in list2:
            commons[j] += 1

        
        for i in commons:
            if commons[i] == 2:
                idx1, idx2 = list1.index(i), list2.index(i)
                sums[idx1 + idx2].append(i)

        _min = min(sums)
        return sums[_min]

        