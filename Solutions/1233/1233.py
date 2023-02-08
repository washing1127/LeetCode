# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2023/2/08 14:40
# File: 1233.py
# Desc: 


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        # print(folder)
        ret = []
        for i in folder:
            flag = True
            for j in ret:
                if i.startswith(j+"/"):
                    flag = False
                    break
            if flag: ret.append(i)
        return ret
