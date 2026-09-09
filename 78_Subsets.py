class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        result = []

        def backtrack(index, current):
            if index == len(nums):
                result.append(current.copy())
                return

            # Include nums[index]
            current.append(nums[index])
            backtrack(index + 1, current)

            # Exclude nums[index]
            current.pop()
            backtrack(index + 1, current)

        backtrack(0, [])

        return result


solution = Solution()

print(solution.subsets([1, 2, 3]))
print(solution.subsets([0]))