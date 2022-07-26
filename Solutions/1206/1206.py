# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/7/26 10:07
# File: 1206.py
# Desc: CV


MAX_LEVEL = 32
P_FACTOR = 0.25

def random_level() -> int:
    lv = 1
    while lv < MAX_LEVEL and random.random() < P_FACTOR:
        lv += 1
    return lv

class SkiplistNode:
    __slots__ = 'val', 'forward'

    def __init__(self, val: int, max_level=MAX_LEVEL):
        self.val = val
        self.forward = [None] * max_level

class Skiplist:
    def __init__(self):
        self.head = SkiplistNode(-1)
        self.level = 0

    def search(self, target: int) -> bool:
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            # �ҵ��� i ��С������ӽ� target ��Ԫ��
            while curr.forward[i] and curr.forward[i].val < target:
                curr = curr.forward[i]
        curr = curr.forward[0]
        # ��⵱ǰԪ�ص�ֵ�Ƿ���� target
        return curr is not None and curr.val == target

    def add(self, num: int) -> None:
        update = [self.head] * MAX_LEVEL
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            # �ҵ��� i ��С������ӽ� num ��Ԫ��
            while curr.forward[i] and curr.forward[i].val < num:
                curr = curr.forward[i]
            update[i] = curr
        lv = random_level()
        self.level = max(self.level, lv)
        new_node = SkiplistNode(num, lv)
        for i in range(lv):
            # �Ե� i ���״̬���и��£�����ǰԪ�ص� forward ָ���µĽڵ�
            new_node.forward[i] = update[i].forward[i]
            update[i].forward[i] = new_node

    def erase(self, num: int) -> bool:
        update = [None] * MAX_LEVEL
        curr = self.head
        for i in range(self.level - 1, -1, -1):
            # �ҵ��� i ��С������ӽ� num ��Ԫ��
            while curr.forward[i] and curr.forward[i].val < num:
                curr = curr.forward[i]
            update[i] = curr
        curr = curr.forward[0]
        if curr is None or curr.val != num:  # ֵ������
            return False
        for i in range(self.level):
            if update[i].forward[i] != curr:
                break
            # �Ե� i ���״̬���и��£��� forward ָ��ɾ���ڵ����һ��
            update[i].forward[i] = curr.forward[i]
        # ���µ�ǰ�� level
        while self.level > 1 and self.head.forward[self.level - 1] is None:
            self.level -= 1
        return True

