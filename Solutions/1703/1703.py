# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/12/18 11:35
# File: 1703.py
# Desc: CV


class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        g, preSum = [], [0]
        for i, num in enumerate(nums):
            if num == 1:
                g.append(i - len(g))
                preSum.append(preSum[-1] + g[-1])
        m, res = len(g), inf
        for i in range(m - k + 1):
            mid = i + k // 2
            r = g[mid]
            res = min(res, (1 - k % 2) * r + (preSum[i + k] - preSum[mid + 1]) - (preSum[mid] - preSum[i]))
        return res

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/minimum-adjacent-swaps-for-k-consecutive-ones/solutions/2024008/de-dao-lian-xu-k-ge-1-de-zui-shao-xiang-mk5ws/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
