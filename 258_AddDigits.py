class Solution:
    def addDigits(self, n: int) -> int:
        while n >= 10:
            total = 0

            while n > 0:
                digit = n % 10
                total += digit
                n //= 10

            n = total

        return n
solution = Solution()
print(solution.addDigits(38))