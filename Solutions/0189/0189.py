# coding=utf-8
# /usr/bin/env python
"""
Author：washing
date：2021/1/8 下午14:56
desc:
"""

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # solution1
        k = k % len(nums)
        nums[:] =  nums[-k:] + nums[:-k]

        # # solution2
        # for _ in range(k):
        #     c = nums[-1]
        #     for i in range(len(nums)-1, -1, -1):
        #         if i == 0: nums[i] = c
        #         else: nums[i] = nums[i-1]

        # solution3
        # ???