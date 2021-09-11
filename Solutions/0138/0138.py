# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/7/22 10:53
# File: 0138.py
# Desc: 
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        return copy.deepcopy(head)