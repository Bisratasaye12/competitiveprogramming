class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        queue1 = deque([i for i,_ in enumerate(senate) if _ == "R"])
        queue2 = deque([j for j,_ in enumerate(senate) if _ == "D"])
        #print(queue1, queue2)

        while queue1 and queue2:
            r, d = queue1.popleft(), queue2.popleft()

            if r < d:
               queue1.append(r + n)
            else:
                queue2.append(d + n)


        if queue1:
            return "Radiant"
        else:
            return "Dire"


