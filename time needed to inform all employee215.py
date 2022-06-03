class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        if n < 2 : return 0
        
        mgrToEmpList = defaultdict(list)
        
        #Build Manager to employee relationship
        for idx, val in enumerate(manager) :
            mgrToEmpList[val].append(idx)
        
        maxNumOfMinutes = 0
        que = deque()
        que.append((headID, informTime[headID]))
        
        while que :
            empId, empInformTime = que.popleft()
            maxNumOfMinutes = max(maxNumOfMinutes, informTime)

            for subId in mgrToEmpList[empId] :
                if subId in mgrToEmpList : 
                    que.append((subId, empInformTime + informTime[subId]))

        return maxNumOfMinutes
