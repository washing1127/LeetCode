# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/6/28 10:18
# File: 0815.py
# Desc: 
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        n = len(routes)
        edge = [[0]*n for _ in range(n)]
        rec = dict()
        for i in range(n):
            for site in routes[i]:
                li = rec.get(site, [])
                for j in li:
                    edge[i][j] = edge[j][i] = True;
                li.append(i)
                rec[site] = li
        dis = [-1] * n
        que = []
        for site in rec.get(source, []):
            dis[site] = 1
            que.append(site)
        while que != []:
            x = que.pop(0)
            for y in range(n):
                if edge[x][y] and dis[y] == -1:
                    dis[y] = dis[x] + 1
                    que.append(y)
        ret = inf
        for site in rec.get(target, []):
            if dis[site] != -1:
                ret = min(ret, dis[site])
        return -1 if ret == inf else ret
