# February 10 2025
# https://leetcode.com/problems/design-underground-system/

class UndergroundSystem:
    checkin = {}
    avg = {}
    def __init__(self):
        self.checkin = {}
        self.avg = {}
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkin[id] = [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation = self.checkin[id][0]
        key = startStation +'_'+ stationName
        if key not in self.avg:
            self.avg[key] = []
        self.avg[key].append(t - self.checkin[id][1])

        self.checkin.pop(id)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = startStation +'_'+ endStation
        size = len(self.avg[key])
        sums = sum(self.avg[key])
        return  sums / size

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)