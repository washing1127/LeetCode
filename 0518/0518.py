# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/6/10 10:53
# File: 0518.py
# Desc: 

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        for coin in coins:
            for i in range(coin, amount+1):
                dp[i] += dp[i - coin]
        return dp[-1]
