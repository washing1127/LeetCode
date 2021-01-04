# coding=utf-8
# /usr/bin/env python
"""
Author：washing
date：2021/1/2 下午11:45
desc:
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        return_link = ListNode(None)
        cur = return_link

        plus = 0
        while l1 or l2:
            if l1:
                v1 = l1.val
                l1 = l1.next
            else:
                v1 = 0
            if l2:
                v2 = l2.val
                l2 = l2.next
            else:
                v2 = 0
            add_together = v1 + v2 + plus
            ans = add_together % 10
            plus = add_together // 10
            if return_link.val == None:
                return_link.val = ans
            else:
                new_node = ListNode(ans)
                cur.next = new_node
                cur = cur.next

        if plus:
            cur.next = ListNode(plus)

        return return_link