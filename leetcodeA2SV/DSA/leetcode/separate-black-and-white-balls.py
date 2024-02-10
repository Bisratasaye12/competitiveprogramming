class Solution:
    def minimumSteps(self, s: str) -> int:
        ph,seeker,n = 0,1, len(s)
        lst = [i for i in s]
        count = 0
        while seeker < n:
            if lst[seeker] == "0" and lst[ph] == "1":
                lst[ph], lst[seeker] = lst[seeker], lst[ph]
                count += (seeker - ph)
                ph += 1                
            elif lst[ph] == "0":
                ph += 1
            
            seeker += 1

        return count

