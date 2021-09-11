# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/2/20 17:12
# File: 0697.py
# Desc: 

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:

        dic = {}
        most_times = 0
        most_length = 50000

        for idx, num in enumerate(nums):
            if num not in dic.keys():
                dic[num] = [idx, 1]
                times = 1
            else:
                times = dic[num][1] + 1
                dic[num][1] = times 
            if times > most_times:
                most_length = idx - dic[num][0]
                most_times = times
            elif times == most_times and idx - dic[num][0] < most_length:
                most_length = idx - dic[num][0]

        return most_length + 1
