# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/2/21 10:21
# File: 1326.py
# Desc: 


class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        rightMost = list(range(n + 1))
        for i, r in enumerate(ranges):
            start = max(0, i - r)
            end = min(n, i + r)
            rightMost[start] = max(rightMost[start], end)

        last = ret = pre = 0
        for i in range(n):
            last = max(last, rightMost[i])
            if i == last:
                return -1
            if i == pre:
                ret += 1
                pre = last
        return ret

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/minimum-number-of-taps-to-open-to-water-a-garden/solutions/101269/guan-gai-hua-yuan-de-zui-shao-shui-long-tou-shu-3/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
