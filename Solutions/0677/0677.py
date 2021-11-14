# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/11/14 23:30
# File: 0677.py
# Desc: 

class MapSum:

    def __init__(self):
        self.d = dict()
        self.old = dict()

    def insert(self, key: str, val: int) -> None:
        subs = ""
        for i in key:
            subs += i
            if subs not in self.d: self.d[subs] = 0
            if key in self.old:
                self.d[subs] -= self.old[key]
            self.d[subs] += val
        self.old[key] = val


    def sum(self, prefix: str) -> int:
        return self.d.get(prefix, 0)


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
