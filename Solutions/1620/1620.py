# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/11/2 11:14
# File: 1620.py
# Desc: 


class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        self.l = [[0]*51 for i in range(51)]
        xma = 0
        yma = 0
        xmi = 51
        ymi = 51
        for x,y,_ in towers:
            xma = max(xma, x)
            yma = max(yma, y)
            xmi = min(xmi, x)
            ymi = min(ymi, y)
        def parse(point):
            x,y,z=point
            for i in range(xmi,xma+1):
                for j in range(ymi,yma+1):
                    jl = sqrt((i-x)**2+(j-y)**2)
                    if jl > radius: self.l[i][j] += 0
                    else: self.l[i][j] += z // (jl+1)
        for p in towers:
            parse(p)
        m = 0
        ret = [0,0]
        for i in range(xmi,xma+1):
            for j in range(ymi,yma+1):
                n = self.l[i][j]
                if n > m: 
                    ret = [i,j]
                    m = n
        return ret
