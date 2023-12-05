class Solution:
    def freqAlphabets(self, s: str) -> str:
       ans = ""
       n = s[::-1]

       i = 0
       while i < len(n):
           if n[i] == "#":
               ans += chr((int(n[i+1:i+3][::-1]) + 96))
               i += 3
           else:
               ans += chr((int(n[i]) + 96))
               i += 1
      

       return ans[::-1]

        

