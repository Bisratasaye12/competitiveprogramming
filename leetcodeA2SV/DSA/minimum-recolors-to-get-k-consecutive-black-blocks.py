class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        count = float('inf')
    
        for i in range(len(blocks)-k+1):
            temp_count = 0
            window = blocks[i:i+k]
            for j in window:
                if j == "W":
                    temp_count += 1
                    
            if temp_count < count:
                count = temp_count
                
        return count
