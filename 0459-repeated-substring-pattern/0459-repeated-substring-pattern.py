class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)

        lps = [0] * n

        length = 0
        i = 1

        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1

            elif length > 0:
                length = lps[length - 1]

            else:
                lps[i] = 0
                i += 1

        longest_prefix_suffix = lps[-1]

        pattern_length = n - longest_prefix_suffix

        return (
            longest_prefix_suffix > 0
            and n % pattern_length == 0
        )