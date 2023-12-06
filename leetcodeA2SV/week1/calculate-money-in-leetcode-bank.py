class Solution:
    def totalMoney(self, n: int) -> int:
        w = math.ceil(n/7)
        total = 0
        
        print(w)
        for i in range(1, w):
            total += (7*i + 21)

        print(total)
        first = w
        rem = 7 if n%7 == 0 else n%7
        last = w + rem - 1
        l = last - first + 1
        ad = l * (last + first) // 2
        print(last, ad)

        return total + ad