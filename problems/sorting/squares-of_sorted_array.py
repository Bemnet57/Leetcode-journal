class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = map(lambda x: x ** 2, nums)
        sortedSquared = sorted(squared)
        return sortedSquared