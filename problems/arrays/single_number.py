class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        for i in range (0,n):
            count = nums.count(nums[i])
            if count == 1:
                return nums[i]