# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/1/4 10:40
# File: 1185.py
# Desc: 

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"][datetime.date(year,month,day).weekday()]
