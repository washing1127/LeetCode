# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/9/24 21:04
# File: 0430.py
# Desc: 

"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""
class Solution:
    def flatten(self, head: 'Node') -> 'Node':
        if not head: return head
        self.ret = None
        def parse(node):
            if not node: return
            new_node = Node(node.val, None, None, None)
            if not self.ret:
                self.cur = self.ret = new_node
            else:
                self.cur.next = new_node
                new_node.prev = self.cur
                self.cur = self.cur.next
            if node.child: parse(node.child)
            if node.next: parse(node.next)

        parse(head)
        return self.ret
        # self.l = []
        # def parse(head):
        #     if not head: return
        #     self.l.append(head.val)
        #     if head.child: parse(head.child)
        #     if head.next: parse(head.next)
        # parse(head)
        # ret = Node(self.l[0],None,None,None)
        # cur = ret
        # for i in self.l[1:]:
        #     node = Node(i, cur, None, None)
        #     cur.next = node
        #     cur = cur.next
        # return ret
