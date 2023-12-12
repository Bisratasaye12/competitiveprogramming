class Solution:
    def isHappy(self, n: int) -> bool:
        cycles = {"4", "16", "37", "58","89", "145", "42", "20"}

        n = str(n)
        while True:
            if n == "1":
                return True
            elif n in cycles:
                return False
            else:
                temp_n = 0
                for i in n:
                    temp_n += (int(i)**2)

                n = str(temp_n)

        
