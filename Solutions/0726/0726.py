# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/7/5 16:39
# File: 0726.py
# Desc: 

class Solution:
    def countOfAtoms(self, formula: str) -> str:
        cnts, multiply, muls, num, num_count, atom = defaultdict(int), 1, [], 0, 0, ""
        for c in formula[::-1]:
            if c == ')':
                if num:
                    multiply *= num
                    muls.append(num)
                    num = num_count = 0
                else:
                    muls.append(1)
            elif c == '(':
                multiply //= muls.pop()
            elif str.isdigit(c):
                num += int(c) * (10 ** num_count)
                num_count += 1
            elif str.islower(c):
                atom += c
            else:
                atom += c
                if num:
                    cnts[atom[::-1]] += num * multiply
                else:
                    cnts[atom[::-1]] += multiply
                atom = ""
                num = num_count = 0
        return "".join(key if cnts[key] == 1 else key + str(cnts[key]) for key in sorted(cnts.keys()))

