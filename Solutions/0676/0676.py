# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/7/11 10:30
# File: 0676.py
# Desc: 


class MagicDictionary:

    def __init__(self):
        pass

    def buildDict(self, dictionary: List[str]) -> None:
        self.l  = dictionary

    def search(self, searchWord: str) -> bool:
        l = list(searchWord)
        n = len(l)
        for i in self.l:
            if searchWord == i or n != len(i): continue
            byy = 0
            for idx in range(n):
                if i[idx] != searchWord[idx]: byy += 1
                if byy >= 2: break
            if byy == 1: return True
        return False



# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dictionary)
# param_2 = obj.search(searchWord)
