class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        
        ones = []
        for i in range(len(boxes)):
            if boxes[i] == "1":
                ones.append(i)

        answer = [0 for i in range(len(boxes))]
   
        for i in range(len(boxes)):
            ops = 0
            for j in ones:
                ops += (abs(i - j))
            answer[i] = ops

        return answer



