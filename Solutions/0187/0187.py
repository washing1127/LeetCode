# coding=utf-8
# /usr/bin/env python
"""
Author：washing
date：2021/10/8 下午13:56
desc:
"""
L = 10

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans = []
        cnt = defaultdict(int)
        for i in range(len(s) - L + 1):
            sub = s[i : i + L]
            cnt[sub] += 1
            if cnt[sub] == 2:
                ans.append(sub)
        return ans

