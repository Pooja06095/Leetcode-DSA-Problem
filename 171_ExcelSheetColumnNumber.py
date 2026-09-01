class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0

        for ch in columnTitle:
            value = ord(ch) - ord('A') + 1
            result = result * 26 + value

        return result
solution = Solution()

print(solution.titleToNumber("A"))
print(solution.titleToNumber("AB"))
print(solution.titleToNumber("ZY"))