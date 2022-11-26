# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/11/26 16:12
# File: 0882.py
# Desc: CV

class Solution:
    def reachableNodes(self, edges: List[List[int]], maxMoves: int, n: int) -> int:
        adList = defaultdict(list)
        for u, v, nodes in edges:
            adList[u].append([v, nodes])
            adList[v].append([u, nodes])
        used = {}
        visited = set()
        reachableNodes = 0
        pq = [[0, 0]]

        while pq and pq[0][0] <= maxMoves:
            step, u = heapq.heappop(pq)
            if u in visited:
                continue
            visited.add(u)
            reachableNodes += 1
            for v, nodes in adList[u]:
                if nodes + step + 1 <= maxMoves and v not in visited:
                    heappush(pq, [nodes + step + 1, v])
                used[(u, v)] = min(nodes, maxMoves - step)

        for u, v, nodes in edges:
            reachableNodes += min(nodes, used.get((u, v), 0) + used.get((v, u), 0))
        return reachableNodes

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/reachable-nodes-in-subdivided-graph/solutions/1990614/xi-fen-tu-zhong-de-ke-dao-da-jie-dian-by-u8m1/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
