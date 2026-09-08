class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        for i in range(1, len(nums)):
            nums[i] = nums[i] + nums[i - 1]

        return nums


solution = Solution()

print(solution.runningSum([1, 2, 3, 4]))
print(solution.runningSum([1, 1, 1, 1, 1]))
print(solution.runningSum([3, 1, 2, 10, 1]))