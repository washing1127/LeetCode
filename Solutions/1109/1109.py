# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/8/31 11:05
# File: 1109.py
# Desc: 


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        nums = [0] * n
        for left, right, inc in bookings:
            nums[left - 1] += inc
            if right < n:
                nums[right] -= inc
    
        for i in range(1, n):
            nums[i] += nums[i - 1]
        
        return nums