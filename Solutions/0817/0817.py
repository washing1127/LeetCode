# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/10/12 11:25
# File: 0817.py
# Desc: 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        nums.sort(key=lambda i: l.index(i))
        ret = 1
        id1 = l.index(nums[0])
        for i in nums:
            new = True
            while i != l[id1]:
                id1 += 1
                if new:
                    ret += 1
                    new = False
            id1 += 1
        return ret
