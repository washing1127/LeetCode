# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/2/11 10:43
# File: 0703.py
# Desc: 

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums.sort(reverse=True)
        self.nums = nums[:k]
        self.k = k

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            for idx, num in enumerate(self.nums):
                if num < val:
                    self.nums.insert(idx, val)
                    break
            else:
                self.nums.append(val)

        elif val > self.nums[-1]:
            self.nums.pop()
            for idx, num in enumerate(self.nums):
                if num < val:
                    self.nums.insert(idx, val)
                    break
            else:
                self.nums.append(val)

        return self.nums[-1]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)