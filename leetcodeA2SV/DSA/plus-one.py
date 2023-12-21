class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        c = 1
        for i in range(len(digits)-1,-1,-1):
            c = (digits[i] + 1) % 10
            if digits[i] + 1 < 10:
                digits[i] += 1
                
                break
            else:
                digits[i] = 0

        
        if c == 0:
            print(c)
            digits.insert(0,1)
        return digits