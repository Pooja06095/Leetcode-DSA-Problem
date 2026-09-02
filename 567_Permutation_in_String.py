def checkInclusion(s1, s2):
    if len(s1) > len(s2):
        return False

    count_s1 = {}
    count_window = {}

    for char in s1:
        count_s1[char] = count_s1.get(char, 0) + 1

    left = 0

    for right in range(len(s2)):
        char = s2[right]
        count_window[char] = count_window.get(char, 0) + 1

        # Window ki length s1 ke equal rakho
        if right - left + 1 > len(s1):
            left_char = s2[left]
            count_window[left_char] -= 1

            if count_window[left_char] == 0:
                del count_window[left_char]

            left += 1

        # Frequencies same hain?
        if count_s1 == count_window:
            return True

    return False


# Function Calling
s1 = "ab"
s2 = "eidbaooo"

answer = checkInclusion(s1, s2)
print(answer)