class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set() # a set to keep track of unique elements
        k = 0 # the writer index/pointer
        for num in nums:
            if num not in seen: #1st occurence of a certain number
                seen.add(num)
                nums[k] = num # keep in place since it's unique
                k += 1 # advance the writer pointer to keep up with the num pointer(the one that checks for uniqueness)
        return k
                