class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        a = duration
        b = timeSeries[0] + duration
        for i in timeSeries[1:]:
            if b <= i: a, b = a+duration, i+duration
            else: a, b = a+duration-b+i, i+duration
        return a
