class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row = 0
        col = len(matrix[0]) - 1

        while row < len(matrix) and col >= 0:
            current = matrix[row][col]

            if current == target:
                return True

            elif current > target:
                col -= 1

            else:
                row += 1

        return False


solution = Solution()

matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]

print(solution.searchMatrix(matrix, 5))
print(solution.searchMatrix(matrix, 20))