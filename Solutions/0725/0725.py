# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/9/22 16:39
# File: 0725.py
# Desc: 

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: ListNode, k: int) -> List[ListNode]:
        l = []
        while head:
            l.append(head.val)
            head = head.next
        n = len(l)
        num = n // k
        ys = n % k
        ret = [None for i in range(k)]
        l_idx = 0
        idx = 0
        while l_idx < k:
            cur = ret[l_idx]
            plus = 0
            if l_idx < ys:
                plus = 1
            for i in range(num+plus):
                if not cur:
                    cur = ret[l_idx] = ListNode(l[idx])
                else:
                    cur.next = ListNode(l[idx])
                    cur = cur.next
                idx += 1
            l_idx += 1
        return ret
