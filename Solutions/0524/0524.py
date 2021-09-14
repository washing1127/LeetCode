# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/9/14 13:56
# File: 0524.py
# Desc: 

class Solution:
    def findLongestWord(self, s: str, dictionary: List[str]) -> str:
        d2 = dictionary.copy()
        for c in s:
            for i in range(len(d2)):
                if d2[i] and d2[i][0] == c:
                    d2[i] = d2[i][1:]
        ret = ''
        for a, b in zip(dictionary, d2):
            if b is '':
                if len(a)>len(ret): ret = a
                elif len(a)==len(ret): ret = min(a, ret)
        return ret

# class Solution:
#     def findLongestWord(self, s: str, dictionary: List[str]) -> str:
#         dictionary.sort(key=lambda x: (-len(x), x))
#         for d in dictionary:
#             i, n = 0, len(d)
#             for j, st in enumerate(s):
#                 if st == d[i]:
#                     i += 1
#                     if i == n:
#                         return d
#         return ""

# class Solution:
#     def findLongestWord(self, s: str, dictionary: List[str]) -> str:
#         m = len(s)
#         f = [[0] * 26 for _ in range(m)]
#         f.append([m] * 26)

#         for i in range(m - 1, -1, -1):
#             for j in range(26):
#                 if ord(s[i]) == j + 97:
#                     f[i][j] = i
#                 else:
#                     f[i][j] = f[i + 1][j]

#         res = ""
#         for t in dictionary:
#             match = True
#             j = 0
#             for i in range(len(t)):
#                 if f[j][ord(t[i]) - 97] == m:
#                     match = False
#                     break
#                 j = f[j][ord(t[i]) - 97] + 1
#             if match:
#                 if len(t) > len(res) or (len(t) == len(res) and t < res):
#                     res = t
#         return res

# class Solution:
#     def findLongestWord(self, s: str, dictionary: List[str]) -> str:
#         res = ""
#         for t in dictionary:
#             i = j = 0
#             while i < len(t) and j < len(s):
#                 if t[i] == s[j]:
#                     i += 1
#                 j += 1
#             if i == len(t):
#                 if len(t) > len(res) or (len(t) == len(res) and t < res):
#                     res = t
#         return res
