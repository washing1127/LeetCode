# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/10/27 8:33
# File: 0301.py
# Desc: 
class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def checkValid(str, lmask, left, rmask, right):
            pos1, pos2 = 0, 0
            cnt = 0

            for i in range(len(str)):
                if pos1 < len(left) and i == left[pos1]:
                    if lmask & (1 << pos1) == 0:
                        cnt += 1
                    pos1 += 1
                elif pos2 < len(right) and i == right[pos2]:
                    if rmask & (1 << pos2) == 0:
                        cnt -= 1
                        if cnt < 0:
                            return False
                    pos2 += 1

            return cnt == 0

        def recoverStr(lmask, left, rmask, right):
            pos1, pos2 = 0, 0
            res = ""

            for i in range(len(s)):
                if pos1 < len(left) and i == left[pos1]:
                    if lmask & (1 << pos1) == 0:
                        res += s[i]
                    pos1 += 1
                elif pos2 < len(right) and i == right[pos2]:
                    if rmask & (1 << pos2) == 0:
                        res += s[i]
                    pos2 += 1
                else:
                    res += s[i]

            return res

        def countBit(x):
            res = 0
            while x != 0:
                x = x & (x - 1)
                res += 1
            return res

        lremove, rremove = 0, 0
        left, right = [], []
        ans = []
        cnt = set()

        for i in range(len(s)):
            if s[i] == '(':
                left.append(i)
                lremove += 1
            elif s[i] == ')':
                right.append(i)
                if lremove == 0:
                    rremove += 1
                else:
                    lremove -= 1

        m, n = len(left), len(right)
        maskArr1, maskArr2 = [], []
        for i in range(1 << m):
            if countBit(i) != lremove:
                continue
            maskArr1.append(i)
        for i in range(1 << n):
            if countBit(i) != rremove:
                continue
            maskArr2.append(i)
        for mask1 in maskArr1:
            for mask2 in maskArr2:
                if checkValid(s, mask1, left, mask2, right):
                    cnt.add(recoverStr(mask1, left, mask2, right))
            
        return [val for val in cnt]


