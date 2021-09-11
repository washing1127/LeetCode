# coding=utf-8
# /usr/bin/env python
"""
Author：washing
date：2021/4/12 下午15:02
desc: 0179.py
"""

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        dic = {}
        for i in nums:
            s = (str(i)*10)[:10]
            if not s in dic.keys(): dic[s] = str(i)
            else: dic[s] += str(i)
        keys = list(dic.keys())
        keys.sort()
        ret = ""
        for key in keys:
            ret = dic[key] + ret
        if set(ret) == {"0"}: return "0"
        else: return ret

        # nums = [str(i) for i in nums]
        # for i in range(len(nums)):
        #     for j in range(i, len(nums)):
        #         if int(nums[i] + nums[j]) < int(nums[j] + nums[i]):
        #             nums[i], nums[j] = nums[j], nums[i]
        # ret = "".join(nums)
        # if set(ret) == {"0"}: return "0"
        # else: return ret