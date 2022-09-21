# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/9/21 10:18
# File: 0854.py
# Desc: CV


class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:
        step, n = 0, len(s1)
        q, vis = [(s1, 0)], {s1}
        while True:
            tmp = q
            q = []
            for s, i in tmp:
                if s == s2:
                    return step
                while i < n and s[i] == s2[i]:
                    i += 1
                for j in range(i + 1, n):
                    if s[j] == s2[i] != s2[j]:  # 剪枝，只在 s[j] != s2[j] 时去交换
                        t = list(s)
                        t[i], t[j] = t[j], t[i]
                        t = ''.join(t)
                        if t not in vis:
                            vis.add(t)
                            q.append((t, i + 1))
            step += 1

