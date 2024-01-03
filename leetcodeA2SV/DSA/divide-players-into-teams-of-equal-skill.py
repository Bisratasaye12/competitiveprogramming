class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        l = 0 
        r = len(skill)-1
        s = skill[l] + skill[r]
        running_sum = 0
        while l < r:
            if skill[l] + skill[r] != s:
                return -1
            else:
                running_sum += (skill[l]*skill[r])
                l += 1
                r -= 1

        return running_sum
            
