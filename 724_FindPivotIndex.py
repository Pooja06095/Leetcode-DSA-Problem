class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        total = sum(nums)
        left_sum = 0

        for i in range(len(nums)):
            right_sum = total - left_sum - nums[i]

            if left_sum == right_sum:
                return i

            left_sum += nums[i]

        return -1


solution = Solution()

print(solution.pivotIndex([1, 7, 3, 6, 5, 6]))
print(solution.pivotIndex([1, 2, 3]))
print(solution.pivotIndex([2, 1, -1]))