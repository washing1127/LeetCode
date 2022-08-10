# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/8/10 17:48
# File: 0640.py
# Desc: 

class Solution:
    def solveEquation(self, equation: str) -> str:
        equation = equation.replace("-", " -").replace("+", " ").replace("=", " = ")
        l = [[], []]
        state = 0
        # print(equation.split(" "))
        for i in equation.split(" "):
            if not i: continue
            if i == "=":
                state = 1
                continue
            if 'x' in i:
                if i == 'x': a = '1'
                elif i=='-x': a='-1'
                else: a = i[:-1]
                if state == 0: l[0].append(int(a))
                else: l[0].append(int(a)*-1)
            else:
                if state == 0: l[1].append(int(i)*-1)
                else: l[1].append(int(i))
        l[1] = sum(l[1])
        l[0] = sum(l[0])
        if l[0] == l[1] == 0: return 'Infinite solutions'
        if l[0] == 0: return 'No solution'
        ans = l[1] / l[0]
        if ans == int(ans): ans = int(ans)
        return 'x='+str(ans)
