class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shift_array = [0]*n

        for st,e,sh in shifts:
            if sh == 1:
                shift_array[st] += 1
                if e < n - 1:
                    shift_array[e+1] -= 1

            else:
                shift_array[st] -= 1
                if e < n - 1:
                    shift_array[e+1] += 1


        r = 0
        res = []
        for i in range(n):
            r += shift_array[i]
            shift_array[i] =  r
            new = chr((ord(s[i]) + shift_array[i] - 97) % 26 + 97)
            res.append(new)

        return "".join(res)

        