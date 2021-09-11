# coding=utf-8
# /usr/bin/env python
"""
Author：washing
date：2021/3/18 下午13:29
desc:
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        count = 1
        cur = head
        flag = True
        if left == 1:
            firstEnd = None
        
        while cur != None:
            if count < left:
                firstEnd = cur
            if count == left:
                subCur = subTail = ListNode(cur.val)
            if right >= count > left:
                newNode = ListNode(cur.val)
                newNode.next = subCur
                subCur = newNode
            if right <= count and flag:
                flag = False
                if firstEnd != None:
                    firstEnd.next = subCur
                else:
                    head = subCur
                subTail.next = cur.next

            count += 1
            cur = cur.next
        return head