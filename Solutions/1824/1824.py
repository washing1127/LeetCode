# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/1/21 21:37
# File: 1824.py
# Desc: 

class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        d = [1, 0, 1]
        for i in range(1, len(obstacles)):
            minCnt = inf
            for j in range(3):
                if j == obstacles[i] - 1:
                    d[j] = inf
                else:
                    minCnt = min(minCnt, d[j])
            for j in range(3):
                if j != obstacles[i] - 1:
                    d[j] = min(d[j], minCnt + 1)
        return min(d)

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/minimum-sideway-jumps/solutions/2070379/zui-shao-ce-tiao-ci-shu-by-leetcode-solu-3y2g/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
