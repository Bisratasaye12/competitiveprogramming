class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        lst = s.split()
        l,m = 0,0
        d = defaultdict(str)
        e = defaultdict(str)
        if len(pattern) != len(lst): return False
        
        while l < len(pattern) and m < len(pattern):
            if pattern[l] in d:
                #print(d)
                if d[pattern[l]] != lst[m]:
                    return False
            else: 
                if lst[m] in e:
                    if e[lst[m]] != pattern[l]:
                        return False
                else:  
                    d[pattern[l]] = lst[m]
                    e[lst[m]] = pattern[l]

            l += 1
            m += 1

        #print(lst, d)

        return True

