class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        """
        traverse over both arrays at once
        if the corresponding values are the different
            check of the value at backs
            if the element at backs has frequency of <1 in fronts
                minimize the integer
            
            check of the value at fronts
            if the element at fronts has frequency of <2 in fronts
                minimize the integer

        
        """
        unflippable = set()
        m = 2000
        for i,j in zip(backs, fronts):
            if i == j:
                unflippable.add(i)

        for u,v in zip(backs, fronts):
            if u != v :
                if u not in unflippable and v not in unflippable:
                    m = min(m, v)
                    m = min(m, u)
                if u in unflippable and v not in unflippable:
                    m = min(m, v)
                if v in unflippable and u not in unflippable:
                    m = min(m, u) 
    
        if m == 2000:
            return 0
        else:
            return m 
