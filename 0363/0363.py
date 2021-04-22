# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/4/22 11:13
# File: 0363.py
# Desc: 


from sortedcontainers import SortedList

class Solution:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        ans = float("-inf")
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            total = [0] * n
            for j in range(i, m): 
                for c in range(n):
                    total[c] += matrix[j][c]
                
                totalSet = SortedList([0])
                s = 0
                for v in total:
                    s += v
                    lb = totalSet.bisect_left(s - k)
                    if lb != len(totalSet):
                        ans = max(ans, s - totalSet[lb])
                    totalSet.add(s)

        return ans

