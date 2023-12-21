class Solution:
    def romanToInt(self, s: str) -> int:
        maps = {"M":1000, "D":500, "C":100, "L": 50, "X":10, "V": 5, "I":1}
        running_sum = 0
        
        i = 0
        while i < len(s):
            if i == len(s)-1 or maps[s[i]] >= maps[s[i+1]]:
                running_sum += maps[s[i]]
                i += 1
            else:
                running_sum += (maps[s[i+1]] - maps[s[i]])
                i += 2

        return running_sum





            
