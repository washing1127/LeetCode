# coding=utf-8
# /usr/bin/env python
"""
Author：washing
date：2021/3/31 下午11:59
desc: 0090.py
"""
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = [[]]
        for i in range(len(nums)):
            for subres in res.copy(): 
                item = subres+[nums[i]]
                item.sort()
                if not item in res:
                    res.append(item)
    
        return res
