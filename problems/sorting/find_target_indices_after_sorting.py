class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        indicesLst = []
        sortedNums= sorted(nums)
        n = len(nums)
        for i in range (0,n):
            if sortedNums[i] == target:
                indicesLst.append(i)
        return indicesLst
      