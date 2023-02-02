# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/2/2 11:05
# File: 1129.py
# Desc: 

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        g = [[] for _ in range(n)]
        for x, y in redEdges:
            g[x].append((y, 0))
        for x, y in blueEdges:
            g[x].append((y, 1))

        dis = [-1] * n
        vis = {(0, 0), (0, 1)}
        q = [(0, 0), (0, 1)]
        level = 0
        while q:
            tmp = q
            q = []
            for x, color in tmp:
                if dis[x] == -1:
                    dis[x] = level
                for p in g[x]:
                    if p[1] != color and p not in vis:
                        vis.add(p)
                        q.append(p)
            level += 1
        return dis

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/shortest-path-with-alternating-colors/solutions/2086543/yan-se-jiao-ti-de-zui-duan-lu-jing-by-le-vnuu/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
