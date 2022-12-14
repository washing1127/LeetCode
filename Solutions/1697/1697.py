# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/12/14 11:02
# File: 1697.py
# Desc: CV

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        edgeList.sort(key=lambda e: e[2])

        # 并查集模板
        fa = list(range(n))
        def find(x: int) -> int:
            if fa[x] != x:
                fa[x] = find(fa[x])
            return fa[x]
        def merge(from_: int, to: int) -> None:
            fa[find(from_)] = find(to)

        ans, k = [False] * len(queries), 0
        # 查询的下标按照 limit 从小到大排序，方便离线
        for i, (p, q, limit) in sorted(enumerate(queries), key=lambda p: p[1][2]):
            while k < len(edgeList) and edgeList[k][2] < limit:
                merge(edgeList[k][0], edgeList[k][1])
                k += 1
            ans[i] = find(p) == find(q)
        return ans

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/checking-existence-of-edge-length-limited-paths/solutions/2018397/jian-cha-bian-chang-du-xian-zhi-de-lu-ji-cdr5/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
