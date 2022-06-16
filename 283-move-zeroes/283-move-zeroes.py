class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(0, n):
            if nums[i] == 0:
                nums.insert(n, 0)
                nums.remove(0)
        print(nums)