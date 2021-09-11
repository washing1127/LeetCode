# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/2/7 18:11
# File: 0665.py
# Desc: 

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 2: return True
        if len(nums) == 3:
            if nums[0]>nums[1]>nums[2]:
                return False
            return True

        flag = nums[1] < nums[0]
        
        for i in range(2, len(nums)):
            if flag:
                if nums[i] < nums[i-1]:
                    return False
            else:
                if nums[i] < nums[i-1]:
                    if nums[i] < nums[i-2]:
                        nums[i] = nums[i-1]
                    else:
                        nums[i-1] = nums[i]
                    flag = True
        return True