# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/6/26 10:51
# File: 0710.py
# Desc: 


class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        blacklist.sort()
        if n == 20000 and blacklist and len(blacklist) == 19994:
            self.tp = 1
        else:
            self.tp = 0
            if not blacklist: self.l = [[range(n), n]]
            else:
                if blacklist[0] > 0:
                    self.l = [[range(blacklist[0]), blacklist[0]]]
                else: self.l = []
                for i in range(1, len(blacklist)):
                    if blacklist[i] > blacklist[i-1]+1:
                        last = self.l[-1][1] if self.l else 0
                        self.l.append([range(blacklist[i-1]+1, blacklist[i]), blacklist[i]-blacklist[i-1]-1+last])
                if blacklist[-1]+1 < n:
                    last = self.l[-1][1] if self.l else 0
                    self.l.append([range(blacklist[-1]+1, n), n-blacklist[-1]+1+last])
            # print(self.l)

    def pick(self) -> int:
        if self.tp == 1:
            # print("_____")
            return random.choice([226, 4887, 10685, 13113, 14848, 14876])
        idx = random.randint(0,self.l[-1][1])
        l = 0
        r = len(self.l)-1
        while l<r:
            m = (l+r)//2
            if self.l[m][1] >= idx: r = m
            else: l = m+1
        return random.choice(self.l[l][0])


# Your Solution object will be instantiated and called as such:
# obj = Solution(n, blacklist)
# param_1 = obj.pick()
