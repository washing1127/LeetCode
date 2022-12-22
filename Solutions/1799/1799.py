# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/12/22 10:47
# File: 1799.py
# Desc: CV


class Solution:
    def maxScore(self, nums: List[int]) -> int:
        L = len(nums)
        N = L // 2
        # i: 第i次操作(从1开始)
        # state: nums中元素的使用情况
        @cache
        def dfs(i, state):
            if i > N: return 0
            # 先获取nums目前可用的元素(下标)
            usable = [j for j in range(L) if state >> j & 1 == 0]
            # 从中任取两个，枚举所有的选取方案，从中取最大值即可
            # combinations函数详解见官方文档
            # https://docs.python.org/zh-cn/3/library/itertools.html?highlight=itertool#itertools.combinations
            return max(i * gcd(nums[a], nums[b]) + dfs(i + 1, state | (1 << a) | (1 << b)) for a, b in combinations(usable, 2))

        return dfs(1, 0)

# class Solution:
#     def maxScore(self, nums: List[int]) -> int:
#         def gys(a,b):
#             if a > b: a,b = b,a
#             while b % a:
#                 a,b = b%a, a
#             return a
#         self.ret = tuple()
#         self.max = 0
#         def parse(before_num=0,before_num_list=None, before_list=None):
#             if before_list is None:
#                 before_list = []
#                 for i in range(len(nums)):
#                     before_list.append(i)
#             if before_num_list is None: before_num_list = []
#             if len(before_list) == 0:
#                 if before_num > self.max:
#                     self.max = before_num
#                     self.ret = before_num_list
#                 return
#             for idx in before_list:
#                 for jdx in before_list:
#                     if jdx <= idx: continue
#                     num = gys(nums[idx],nums[jdx])
#                     next_list = before_list.copy()
#                     next_list.remove(jdx)
#                     next_list.remove(idx)
#                     next_num = before_num_list.copy()
#                     next_num.append(num)
#                     parse(before_num+num,next_num, next_list)
#         parse()
#         self.ret.sort()
#         ret = 0
#         for idx,i in enumerate(self.ret):
#             ret += i*(idx+1)
#         return ret
