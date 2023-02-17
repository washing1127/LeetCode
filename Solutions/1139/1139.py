# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/2/17 11:05
# File: 1139.py
# Desc: 


class Solution:
    def largest1BorderedSquare(self, grid):
        m, n = len(grid), len(grid[0])
        left = [[0] * (n + 1) for _ in range(m + 1)]
        up = [[0] * (n + 1) for _ in range(m + 1)]
        maxBorder = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if grid[i - 1][j - 1]:
                    left[i][j] = left[i][j - 1] + 1
                    up[i][j] = up[i - 1][j] + 1
                    border = min(left[i][j], up[i][j])
                    while left[i - border + 1][j] < border or up[i][j - border + 1] < border:
                        border -= 1
                    maxBorder = max(maxBorder, border)
        return maxBorder ** 2

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/largest-1-bordered-square/solutions/2114369/zui-da-de-yi-1-wei-bian-jie-de-zheng-fan-74ce/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
