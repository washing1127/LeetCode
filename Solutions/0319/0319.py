class Solution:
    def bulbSwitch(self, n: int) -> int:
        # i = 0
        # while i*(i+2) < n:
        #     i += 1
        # return i
        return int(math.sqrt(n))
