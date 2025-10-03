class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        sortedUnique = sorted(uniqueNums, reverse = True)
        n = len(sortedUnique)
        if n >= 3:
            return sortedUnique[2]
        else:
            return max(sortedUnique)