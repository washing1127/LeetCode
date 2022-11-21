# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/11/21 10:12
# File: 0808.py
# Desc: CV

class Solution:
    def soupServings(self, n: int) -> float:
        n = (n + 24) // 25
        if n >= 179:
            return 1.0
        @cache
        def dfs(a: int, b: int) -> float:
            if a <= 0 and b <= 0:
                return 0.5
            if a <= 0:
                return 1.0
            if b <= 0:
                return 0.0
            return (dfs(a - 4, b) + dfs(a - 3, b - 1) +
                    dfs(a - 2, b - 2) + dfs(a - 1, b - 3)) / 4
        return dfs(n, n)

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/soup-servings/solutions/1981704/fen-tang-by-leetcode-solution-0yxs/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
