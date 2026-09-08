class Solution:
    def sortByBits(self, arr: list[int]) -> list[int]:
        def count_bits(num):
            count = 0

            while num > 0:
                count += num & 1
                num >>= 1

            return count

        arr.sort(key=lambda x: (count_bits(x), x))

        return arr


solution = Solution()

print(solution.sortByBits([0, 1, 2, 3, 4, 5, 6, 7, 8]))
print(solution.sortByBits([1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]))