class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        p = len(arr)
        k_list = []
        new = arr

        while p > 0:
            idx = 0
            m = new[0]
            for i in range(p):
                if new[i] > m:
                    m = new[i]
                    idx = i

            #print(m, idx, p, new)

            k_list.append(idx + 1)
            k_list.append(p)
            n = new[:idx+1][::-1] + new[idx+1:p]
            new[:p] = n[::-1]

            #print(n, new)
            p -= 1


        return k_list

            

