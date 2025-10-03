class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numRange = len(nums)
        for i in range (0, numRange+1):
            if i not in nums:
                return i
            else:
                continue
        