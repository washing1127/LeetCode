class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        c = collections.Counter(nums)
        ret = []
        for k,v in c.items():
            if v > len(nums) // 3:
                ret.append(k)
        return ret
