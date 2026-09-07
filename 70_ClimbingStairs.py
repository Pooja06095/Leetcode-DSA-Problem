class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        first = 1
        second = 2

        for i in range(3, n + 1):
            third = first + second
            first = second
            second = third

        return second


solution = Solution()

print(solution.climbStairs(2))
print(solution.climbStairs(3))
print(solution.climbStairs(5))