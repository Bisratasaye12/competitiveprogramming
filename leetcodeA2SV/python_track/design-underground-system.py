class UndergroundSystem:

    def __init__(self):
        self.travel_time = defaultdict(list) # Maps the s1-s2 to it's duration to travel from s1 to s2 and count of the journeys
        self.check_ins = defaultdict(list) # Maps id of customer to the station checked in and time at checked in
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id].append(stationName)
        self.check_ins[id].append(t)

        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        journey = self.check_ins[id][0] + "_"+ stationName
        t1 = self.check_ins[id][1]
        self.check_ins[id].clear()
        if self.travel_time[journey]:
            self.travel_time[journey][0] += (t - t1)
            self.travel_time[journey][1] += 1
        else:
            self.travel_time[journey].append(t-t1)
            self.travel_time[journey].append(1)


    def getAverageTime(self, startStation: str, endStation: str) -> float:
        journey = startStation + "_"+ endStation
        _sum = self.travel_time[journey][0]
        no_of_journeys = self.travel_time[journey][1]
        return _sum / no_of_journeys
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)