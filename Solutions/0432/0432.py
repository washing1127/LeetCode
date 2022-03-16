# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/3/16 10:14
# File: 0432.py
# Desc: 

class Node:
    def __init__(self, key="", count=0):
        self.prev = None
        self.next = None
        self.keys = {key}
        self.count = count

    def insert(self, node: 'Node') -> 'Node':  # 在 self 后插入 node
        node.prev = self
        node.next = self.next
        node.prev.next = node
        node.next.prev = node
        return node

    def remove(self):  # 从链表中移除 self
        self.prev.next = self.next
        self.next.prev = self.prev

class AllOne:
    def __init__(self):
        self.root = Node()
        self.root.prev = self.root
        self.root.next = self.root  # 初始化链表哨兵，下面判断节点的 next 若为 self.root，则表示 next 为空（prev 同理）
        self.nodes = {}

    def inc(self, key: str) -> None:
        if key not in self.nodes:  # key 不在链表中
            if self.root.next is self.root or self.root.next.count > 1:
                self.nodes[key] = self.root.insert(Node(key, 1))
            else:
                self.root.next.keys.add(key)
                self.nodes[key] = self.root.next
        else:
            cur = self.nodes[key]
            nxt = cur.next
            if nxt is self.root or nxt.count > cur.count + 1:
                self.nodes[key] = cur.insert(Node(key, cur.count + 1))
            else:
                nxt.keys.add(key)
                self.nodes[key] = nxt
            cur.keys.remove(key)
            if len(cur.keys) == 0:
                cur.remove()

    def dec(self, key: str) -> None:
        cur = self.nodes[key]
        if cur.count == 1:  # key 仅出现一次，将其移出 nodes
            del self.nodes[key]
        else:
            pre = cur.prev
            if pre is self.root or pre.count < cur.count - 1:
                self.nodes[key] = cur.prev.insert(Node(key, cur.count - 1))
            else:
                pre.keys.add(key)
                self.nodes[key] = pre
        cur.keys.remove(key)
        if len(cur.keys) == 0:
            cur.remove()

    def getMaxKey(self) -> str:
        return next(iter(self.root.prev.keys)) if self.root.prev is not self.root else ""

    def getMinKey(self) -> str:
        return next(iter(self.root.next.keys)) if self.root.next is not self.root else ""



# class AllOne:

#     def __init__(self):
#         self.dic = defaultdict(int)
#         self.change = True
#         self.ma = ''
#         self.mi = ''

#     def inc(self, key: str) -> None:
#         self.dic[key] += 1
#         self.change = True

#     def dec(self, key: str) -> None:
#         self.dic[key] -= 1
#         if self.dic[key] == 0: del self.dic[key]
#         self.change = True

#     def getMaxKey(self) -> str:
#         if not self.change: return self.ma
#         l = sorted(self.dic.values())
#         # print(self.dic)
#         if not l: return ""
#         for k,v in self.dic.items():
#             if v == l[-1]:
#                 self.ma = k
#                 return k

#     def getMinKey(self) -> str:
#         if not self.change: return self.mi
#         l = sorted(self.dic.values())
#         if not l: return ""
#         for k,v in self.dic.items():
#             if v == l[0]:
#                 self.mi = k
#                 return k


# # Your AllOne object will be instantiated and called as such:
# # obj = AllOne()
# # obj.inc(key)
# # obj.dec(key)
# # param_3 = obj.getMaxKey()
# # param_4 = obj.getMinKey()
