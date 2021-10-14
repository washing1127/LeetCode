class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if len(arr) == 3: return 1
        l, r = 1, len(arr)-1
        while l < r:
            m = (l+r)//2
            if arr[m-1]<arr[m]>arr[m+1]:
                return m
            elif arr[m-1]>arr[m]: r = m
            else: l = m+1
        return l
