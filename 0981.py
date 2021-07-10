class TimeMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dict = dict()


    def set(self, key: str, value: str, timestamp: int) -> None:
        if not key in self.dict: self.dict[key] = list()
        self.dict[key].append([timestamp, value])


    def get(self, key: str, timestamp: int) -> str:
        if not key in self.dict.keys(): return ""
        li = self.dict[key]
        l = 0; r = len(li)-1
        if li[l][0] > timestamp: return ""
        while l < r:
            m = (l + r + 1) // 2
            if li[m][0] <= timestamp:
                l = m 
            else:
                r = m - 1
        return li[l][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
