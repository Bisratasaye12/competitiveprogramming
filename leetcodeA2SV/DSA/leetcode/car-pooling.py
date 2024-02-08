class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        n = max(trips, key= lambda x: x[2])[2] + 1
        
        carSeats = [0] * n

        for Npass, f, t in trips:
            carSeats[f] += Npass
            carSeats[t] -= Npass
        #print(carSeats)
        for i in range(1, n):
            carSeats[i] += carSeats[i-1]

        #print(carSeats)  
        for i in carSeats:
            if i > capacity:
                #print(i)
                return False
        else:
            return True
