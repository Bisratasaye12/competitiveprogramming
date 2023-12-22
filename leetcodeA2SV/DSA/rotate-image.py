from collections import defaultdict
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        mapp = defaultdict(int)
        for row in range(n):
            for col in range(n):
                row2 = col
                col2 = (n-1) - row
                mapp[(row2, col2)] = matrix[row][col]


        for row,col in mapp:
            matrix[row][col] = mapp[(row,col)]




        """   col2 = (n-1) - row1    
              row2 = col1
        """

        



        
          

        