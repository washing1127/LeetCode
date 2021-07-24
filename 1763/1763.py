# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/7/24 23:03
# File: 1763.py
# Desc: 
class Solution:
    def maximumTime(self, time: str) -> str:
        ret = ""
        if time[0] == "?":
            if time[1] in "456789":
                ret += "1"
                ret += time[1]
            else:
                ret += "2"
                if time[1] == "?":
                    ret += "3"
                else: ret += time[1]
        elif time[0] == "2":
            if time[1] == "?":
                ret += "23"
            else:
                ret += time[:2]
        else:
            ret += time[0]
            if time[1] == "?": ret += "9"
            else: ret += time[1]
        ret += ":"
        if time[3] == "?": ret += "5"
        else: ret += time[3]
        if time[4] == "?": ret += "9"
        else: ret += time[4]

        return ret 
