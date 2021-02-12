# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/2/12 11:06
# File: 0119.py
# Desc: 
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        last_list = self.getRow(rowIndex-1)
        li = [1]
        for idx in range(1, len(last_list)):
            li.append(last_list[idx]+last_list[idx-1])
        li.append(1)

        return li