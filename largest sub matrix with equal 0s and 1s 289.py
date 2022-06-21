from typing import List


def largestSubMatrix(n: int, m: int, arr: List[List[int]]):

    maxArea = 0
    for topR in range(n):
        for topC in range(m):
            for bottomR in range(topR, n):
                for bottomC in range(topC, m):
                    cnt0 = 0
                    cnt1 = 0

                    for i in range(topR, bottomR + 1):
                        for j in range(topC, bottomC + 1):
                            if arr[i][j] == 0:
                                cnt0 += 1
                            else:
                                cnt1 += 1

                    if(cnt0 == cnt1):
                        area = (bottomR-topR+1)*(bottomC-topC+1)
                        maxArea = max(maxArea, area)

    return maxArea
