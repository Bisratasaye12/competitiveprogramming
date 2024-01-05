class Solution:
    def isLongPressedName(self, name: str, typed: str) -> bool:
        n, m = len(name), len(typed)
        if n > m: return False
        l, r = 0,0

        while l < n and r < m:
            if typed[r] == name[l]:
                l += 1
                r += 1
            elif l != 0 and typed[r] == name[l-1]:
                r += 1
            else:
                return False

    
        while r < m:
            if typed[r] != name[-1]:
                return False
            r += 1
    
        while l < n:
            if name[l] != typed[-1]:
                return False
            l += 1

        return True