class Solution(object):
    def leastInterval(self, tasks, n):
        counters = {}
        maxCounter = 0
        
        for task in tasks:
            counters[task] = counters.get(task, 0) + 1
            maxCounter = max(counters[task], maxCounter)
                
        numOfMax = 0
    
        for value in counters.values():
            if value == maxCounter:
                numOfMax += 1

        numOfChunks = maxCounter - 1
        chunkSize = n + 1        
        
        sizeOfAllChunks = numOfChunks * chunkSize + numOfMax
        
        return max(len(tasks), sizeOfAllChunks)
