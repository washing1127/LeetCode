# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/11/30 10:05
# File: 0895.py
# Desc: CV

class FreqStack:
    def __init__(self):
        self.freq = defaultdict(int)
        self.group = defaultdict(list)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        self.freq[val] += 1
        self.group[self.freq[val]].append(val)
        self.maxFreq = max(self.maxFreq, self.freq[val])

    def pop(self) -> int:
        val = self.group[self.maxFreq].pop()
        self.freq[val] -= 1
        if len(self.group[self.maxFreq]) == 0:
            self.maxFreq -= 1
        return val

# 作者：力扣官方题解
# 链接：https://leetcode.cn/problems/maximum-frequency-stack/solutions/1997251/zui-da-pin-lu-zhan-by-leetcode-solution-moay/
# 来源：力扣（LeetCode）
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
