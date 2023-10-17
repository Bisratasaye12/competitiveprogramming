#User function Template for python3

class Solution:
    def arraySortedOrNot(self, arr, n):
        # code here
        p = 0
        q = 1
        
        while q < n:
            if arr[p] > arr[q]:
                return False
            q += 1
            p += 1
            
        return True
