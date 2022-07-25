# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/7/25 10:11
# File: 0919.py
# Desc: 


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        temp = []
        def parse(root, level=0):
            if root.left: parse(root.left, level+1)
            if root.right: parse(root.right, level+1)
            if not root.left or not root.right: temp.append([root,level])
        parse(root)
        temp.sort(key=lambda x: x[1])
        self.l = [i[0] for i in temp]
        # print(self.l)


    def insert(self, val: int) -> int:
        temp = self.l[0]
        tr = TreeNode(val=val)
        if not temp.left:
            temp.left = tr
        else:
            temp.right = tr
            self.l.pop(0)
        self.l.append(tr)
        return temp.val


    def get_root(self) -> TreeNode:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()
