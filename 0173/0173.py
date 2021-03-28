# coding=utf-8
# /usr/bin/env python
"""
Author：washing
date：2021/3/28 下午21:22
desc:
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.stack = []
        while root:
            self.stack.append(root)
            root = root.left

    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        temp = self.stack.pop()
        res = temp.val
        temp = temp.right
        while temp:
            self.stack.append(temp)
            temp = temp.left
        return res

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        return self.stack != []


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()