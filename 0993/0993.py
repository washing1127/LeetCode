# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/5/17 10:10
# File: 0993.py
# Desc: 

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        dic = {}
        def dd(root, count, father):
            if count not in dic.keys(): dic[count] = {}
            dic[count][root.val] = father

            if root.left != None:
                dd(root.left, count+1, root.val)
            if root.right != None:
                dd(root.right, count+1, root.val)

        dd(root, 1, None)

        for d in dic.values():
            if x in d.keys() and y in d.keys() and d[x] != d[y]:
                return True
        return False