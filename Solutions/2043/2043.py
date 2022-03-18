# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/3/18 10:02
# File: 2043.py
# Desc: 

class Bank:

    def __init__(self, balance: List[int]):
        self.l = [0]+balance
        self.n = len(balance)


    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > self.n or self.l[account1] < money or account2 > self.n: return False
        self.l[account1] -= money
        self.l[account2] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        if account > self.n: return False
        self.l[account] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        if account > self.n or self.l[account] < money: return False
        self.l[account] -= money
        return True


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)
