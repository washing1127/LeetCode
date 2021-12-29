class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        n = len(chalk)
        s = sum(chalk)
        k = k % s
        idx = 0
        while True:
            k -= chalk[idx]
            if k < 0:
                return idx
            idx += 1
            if idx == n: idx=0
