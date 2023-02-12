# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/2/12 11:05
# File: 1138.py
# Desc: 


class Solution:
    def alphabetBoardPath(self, target: str) -> str:
        c = 0
        r = 0
        ret = ""
        board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]
        for i in target:
            for newr in range(len(board)):
                if i in board[newr]:
                    newc = board[newr].index(i)
                    if i == 'z':
                        if newc >= c:
                            ret += "R" * (newc - c)
                        else:
                            ret += "L" * (c - newc)
                        if newr >= r:
                            ret += "D" * (newr - r)
                        else:
                            ret += "U" * (r - newr)
                    else:
                        if newr >= r:
                            ret += "D" * (newr - r)
                        else:
                            ret += "U" * (r - newr)
                        if newc >= c:
                            ret += "R" * (newc - c)
                        else:
                            ret += "L" * (c - newc)
                    r = newr
                    c = newc
                    ret += "!"
                    break
        return ret
