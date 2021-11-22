# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/11/22 13:29
# File: 0384.py
# Desc: 


class Solution:

    def __init__(self, nums: List[int]):
        self.nums1 = nums
        self.nums2 = nums.copy()

    def reset(self) -> List[int]:
        return self.nums2

    def shuffle(self) -> List[int]:
        random.shuffle(self.nums1)
        return self.nums1



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
