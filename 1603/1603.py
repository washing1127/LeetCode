# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2021/3/19 10:29
# File: 1603.py
# Desc: 
class ParkingSystem:

    def __init__(self, big: int, medium: int, small: int):
        self.dic = {1:big, 2:medium, 3:small}

    def addCar(self, carType: int) -> bool:
        if self.dic[carType] >= 1:
            self.dic[carType] -= 1
            return True
        else:
            return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)