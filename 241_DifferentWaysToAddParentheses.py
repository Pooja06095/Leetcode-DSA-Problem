class Solution:
    def diffWaysToCompute(self, expression: str) -> list[int]:

        def compute(exp):
            results = []

            for i in range(len(exp)):
                if exp[i] in "+-*":
                    left_results = compute(exp[:i])
                    right_results = compute(exp[i + 1:])

                    for left in left_results:
                        for right in right_results:
                            if exp[i] == "+":
                                results.append(left + right)
                            elif exp[i] == "-":
                                results.append(left - right)
                            else:
                                results.append(left * right)

            # If there is no operator, exp is just a number
            if not results:
                results.append(int(exp))

            return results

        return compute(expression)


solution = Solution()

print(solution.diffWaysToCompute("2-1-1"))
print(solution.diffWaysToCompute("2*3-4*5"))