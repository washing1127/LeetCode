# coding=utf-8
# /usr/bin/env python
"""
Author：washing
date：2022/1/10 9:58
desc: 0089.py
"""

class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0]
        for i in range(1, n + 1):
            for j in range(len(ans) - 1, -1, -1):
                ans.append(ans[j] | (1 << (i - 1)))
        return ans

