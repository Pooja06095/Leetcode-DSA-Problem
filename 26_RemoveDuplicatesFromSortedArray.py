class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k


solution = Solution()

nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]

k = solution.removeDuplicates(nums)

print("k =", k)
print("nums =", nums[:k])