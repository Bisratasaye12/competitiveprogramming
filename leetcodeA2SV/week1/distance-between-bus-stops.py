class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        adj_list = []
        n = len(distance)
        for i in range(n):
            if i == 0 :
                adj_list.append([n-1, 1])
            elif i == n-1:
                adj_list.append([n-2, 0])
            else:
                adj_list.append([i-1, i+1])


        curr = start
        a_d = 0
        while curr != destination:
            curr = adj_list[curr][0]
            a_d += distance[curr]

        curr = start
        c_d = 0
        while curr != destination:
            c_d += distance[curr]
            curr = adj_list[curr][1]

        return min(a_d, c_d)


            
        return 0
            