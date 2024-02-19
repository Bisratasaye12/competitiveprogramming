class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        prevS, nextS = [-1]*n, [n]*n

        stack = []

        for i in range(n):

            while stack and arr[stack[-1]] > arr[i]:
                elm = stack.pop()

            if stack:
                prevS[i] = stack[-1]

            stack.append(i)

        stack = []

        for i in range(n):
            while stack and arr[stack[-1]] > arr[i]:
                elm = stack.pop()

                nextS[elm] = i

            stack.append(i)

        ans = 0

        for i in range(n):
            p,nxt = prevS[i], nextS[i]

            left = i - p
            right = nxt - i 
            ans += (((left) * right) * arr[i])

        #print(prevS, nextS)
        return ans % (10 **9 + 7)






