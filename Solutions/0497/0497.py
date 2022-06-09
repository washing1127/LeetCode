class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.l = []
        num = 0
        for (x1,y1,x2,y2) in self.rects:
            num += (y2-y1+1)*(x2-x1+1)
            self.l.append(num)

    def pick(self) -> List[int]:
        num = random.randint(0,self.l[-1])
        idx = 0
        for i in self.l:
            if i < num: idx += 1
        x1,y1,x2,y2 = self.rects[idx]
        x = random.randint(x1,x2)
        y = random.randint(y1,y2)
        return [x,y]


# Your Solution object will be instantiated and called as such:
# obj = Solution(rects)
# param_1 = obj.pick()
