class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
      
        temp = dict()
        
        if len(s) == len(t):
            j = 0
            for i in s:
                if i in temp:
                    temp[i] += 1
                else:
                    temp[i] = 1
                    
                if t[j] in temp:
                    temp[t[j]] -= 1
                else:
                    temp[t[j]] = -1
                j += 1


            for i in s:
                if temp[i] != 0:
                    return False
            return True
        return False
            
                
        
