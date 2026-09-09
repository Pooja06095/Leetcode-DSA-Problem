class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        ones = 0
        twos = 0

        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones

        return ones


solution = Solution()

print(solution.singleNumber([2, 2, 3, 2]))
print(solution.singleNumber([0, 1, 0, 1, 0, 1, 99]))