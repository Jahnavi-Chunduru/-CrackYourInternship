import heapq 
class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        max_heap = []
        stops  = 0
        cfuel = startFuel
        for station in stations:
            pos = station[0]
            fuel = station[1]
            while(cfuel < pos):
                if len(max_heap) ==0 :
                    return -1
                x = heappop(max_heap)
                cfuel += (-x)
                stops += 1
            heappush(max_heap , -fuel)
        while(cfuel < target):
            if len(max_heap) ==0 :
                return -1
            x = heappop(max_heap)
            cfuel += -x
            stops += 1
        return stops
