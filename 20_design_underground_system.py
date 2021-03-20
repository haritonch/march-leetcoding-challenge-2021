class UndergroundSystem:

    def __init__(self):
        self.time = {} # {(start, end): [times]}
        self.check_in = {} # {id: {time: t, station: s}}
        
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = {'time': t, 'station': stationName}

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        check_in_time = self.check_in[id]['time']
        check_in_station = self.check_in[id]['station']
        if (check_in_station, stationName) not in self.time:
            self.time[(check_in_station, stationName)] = []
        self.time[(check_in_station, stationName)].append(t - check_in_time)
        del self.check_in[id] # checked out

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.time[(startStation, endStation)]
        return sum(times) / len(times)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)