class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        write_ptr = 0
        for read_ptr in range(len(nums)):
            
            current_num = nums[read_ptr]
            if current_num != 0:
                if read_ptr != write_ptr:
                    nums[write_ptr], nums[read_ptr] = nums[read_ptr], nums[write_ptr]
                write_ptr += 1
       