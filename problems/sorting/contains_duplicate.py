class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniqueNums = set(nums)
        if len(nums) != len(uniqueNums):
            return True
        else:
            return False
        