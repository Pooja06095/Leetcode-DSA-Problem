class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 2 ==0:
            n = n//2

        return n == 1
    
solution = Solution()

print(solution.isPowerOfTwo(16))
print(solution.isPowerOfTwo(12))