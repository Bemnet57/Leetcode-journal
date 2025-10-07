class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right: 
            mid = (left + right)//2 # calculate mid inside the loop so when the pointers update it updates too
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid # keep mid as potential insert position, since integer division approximates it's position to the right(hypothesis), and not skip the former mid position from getting skipped unchecked 
        if left == right:
            return left