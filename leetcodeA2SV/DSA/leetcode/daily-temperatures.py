class Solution:
    def dailyTemperatures(self, temperatures):
        stack = []

        ans = [0]*len(temperatures)

        for i in range(len(temperatures)):
            
            while stack and temperatures[stack[-1]] < temperatures[i]:
                elem = stack.pop()
                
                ans[elem] = i - elem
            
            stack.append(i)

        
        return ans 

            