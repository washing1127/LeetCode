# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/1/29 10:03
# File: 1765.py
# Desc: CV

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        ans = [[water - 1 for water in row] for row in isWater]
        q = deque((i, j) for i, row in enumerate(isWater) for j, water in enumerate(row) if water)  # 将所有水域入队
        while q:
            i, j = q.popleft()
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                if 0 <= x < m and 0 <= y < n and ans[x][y] == -1:
                    ans[x][y] = ans[i][j] + 1
                    q.append((x, y))
        return ans

