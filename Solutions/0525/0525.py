# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/6/4 13:56
# File: 0525.py
# Desc: 

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        hashmap = {0:-1}
        counter = ans = 0
        for i,num in enumerate(nums):
            if num:
                counter += 1
            else:
                counter -= 1
            if counter in hashmap:
                ans = max(ans, i - hashmap[counter])
            else:
                hashmap[counter] = i
        return ans

