def characterReplacement(s, k):
    count = {}
    left = 0
    max_frequency = 0
    max_length = 0

    for right in range(len(s)):
        char = s[right]

        count[char] = count.get(char, 0) + 1
        max_frequency = max(max_frequency, count[char])

        window_length = right - left + 1

        if window_length - max_frequency > k:
            count[s[left]] -= 1
            left += 1

        window_length = right - left + 1
        max_length = max(max_length, window_length)

    return max_length


# Function Calling
s = "ABAB"
k = 2

answer = characterReplacement(s, k)
print(answer)