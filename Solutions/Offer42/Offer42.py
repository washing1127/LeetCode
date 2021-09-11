class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        pre = 0
        m = nums[0]
        for x in nums:
            pre = max(pre+x, x)
            m = max(m, pre)
        return m