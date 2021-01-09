# coding=utf-8
# /usr/bin/env python
"""
Author：washing
date：2021/1/9 下午15:41
desc:
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2[:]
        nums1.sort()