# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/6/13 23:49
# File: 0278.py
# Desc: 

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        r = n
        while l < r:
            m = (l + r) // 2
            if isBadVersion(m):
                r = m
            else: l = m + 1

        return l
