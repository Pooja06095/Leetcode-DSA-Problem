class Solution:
    def numberOfSteps(self, num: int) -> int:
        steps = 0

        while num > 0:
            if num % 2 == 0:
                num //= 2
            else:
                num -= 1

            steps += 1

        return steps


solution = Solution()

print(solution.numberOfSteps(14))
print(solution.numberOfSteps(8))
print(solution.numberOfSteps(123))