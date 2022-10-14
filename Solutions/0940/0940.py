# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/10/14 10:48
# File: 0940.py
# Desc: CV

class Solution:
    def distinctSubseqII(self, s: str) -> int:
        mod = 10**9 + 7
        last = [-1] * 26

        n = len(s)
        f = [1] * n
        for i, ch in enumerate(s):
            for j in range(26):
                if last[j] != -1:
                    f[i] = (f[i] + f[last[j]]) % mod
            last[ord(s[i]) - ord("a")] = i

        ans = 0
        for i in range(26):
            if last[i] != -1:
                ans = (ans + f[last[i]]) % mod
        return ans

# 作者：LeetCode-Solution
# 链接：https://leetcode.cn/problems/distinct-subsequences-ii/solution/bu-tong-de-zi-xu-lie-ii-by-leetcode-solu-k2h5/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
