# -*- coding:utf-8 -*-
# Author: washing
# DateTime: 2022/1/23 15:16
# File: 2034.py
# Desc: 

class StockPrice:
    def __init__(self):
        self.maxPrice = []
        self.minPrice = []
        self.timePriceMap = {}
        self.maxTimestamp = 0

    def update(self, timestamp: int, price: int) -> None:
        heappush(self.maxPrice, (-price, timestamp))
        heappush(self.minPrice, (price, timestamp))
        self.timePriceMap[timestamp] = price
        self.maxTimestamp = max(self.maxTimestamp, timestamp)

    def current(self) -> int:
        return self.timePriceMap[self.maxTimestamp]

    def maximum(self) -> int:
        while True:
            price, timestamp = self.maxPrice[0]
            if -price == self.timePriceMap[timestamp]:
                return -price
            heappop(self.maxPrice)

    def minimum(self) -> int:
        while True:
            price, timestamp = self.minPrice[0]
            if price == self.timePriceMap[timestamp]:
                return price
            heappop(self.minPrice)
