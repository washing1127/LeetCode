# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/11/2 10:33
# File: 0237.py
# Desc: 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val;
        node.next = node.next.next
