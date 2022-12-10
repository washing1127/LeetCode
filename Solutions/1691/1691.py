# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/12/10 17:52
# File: 1691.py
# Desc: CV

class Solution:
    def maxHeight(self, cuboids: List[List[int]]) -> int:
        n = len(cuboids)
        for c in cuboids:
            c.sort()
        cuboids.sort(key=sum)
        ans = 0
        dp = [0] * n
        for i in range(n):
            dp[i] = cuboids[i][2]
            for j in range(i):
                if cuboids[i][0] >= cuboids[j][0] and cuboids[i][1] >= cuboids[j][1] and cuboids[i][2] >= cuboids[j][2]:
                    dp[i] = max(dp[i], dp[j] + cuboids[i][2])
            ans = max(ans, dp[i])
        return ans

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/maximum-height-by-stacking-cuboids/solutions/2013994/dui-die-chang-fang-ti-de-zui-da-gao-du-b-17qg/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
