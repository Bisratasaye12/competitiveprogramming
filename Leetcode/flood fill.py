class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m,n = len(image),len(image[0])
        dirc = [(0,1), (0,-1), (1,0), (-1,0)]
        def inbound(r,c):
            return 0<=r<m and 0<=c<n
            
        if image[sr][sc] == color:
            return image
        queue = deque([(sr,sc)])
        visited = set((sr,sc))
        sColor = image[sr][sc]
        while queue:
            x,y = queue.popleft()
            image[x][y] = color
            for dx, dy in dirc:
                nx, ny = dx + x , dy + y
                if inbound(nx,ny) and (nx, ny) not in visited and image[nx][ny] == sColor:
                    image[nx][ny] = color
                    queue.append((nx,ny))
                    visited.add((nx, ny)) 

        return image
