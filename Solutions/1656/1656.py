# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/8/16 10:40
# File: 1656.py
# Desc: 


class OrderedStream:

    def __init__(self, n: int):
        self.l = [''] * n
        self.pos = 0

    def insert(self, idKey: int, value: str) -> List[str]:
        ret = []
        self.l[idKey-1] = value
        pos = self.pos
        while pos < len(self.l) and self.l[pos] != '':
            ret.append(self.l[pos])
            pos += 1
        if ret: self.pos = pos
        return ret



# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
