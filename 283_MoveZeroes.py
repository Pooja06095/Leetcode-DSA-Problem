class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        index = 0

        # Move all non-zero elements to the front
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[index] = nums[i]
                index += 1

        # Fill remaining positions with zero
        while index < len(nums):
            nums[index] = 0
            index += 1


solution = Solution()

nums = [0, 1, 0, 3, 12]
solution.moveZeroes(nums)

print(nums)