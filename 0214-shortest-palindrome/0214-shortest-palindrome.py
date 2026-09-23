class Solution:
    def shortestPalindrome(self, s: str) -> str:

        # Reverse the string
        rev = s[::-1]

        # Combine original + separator + reverse
        combined = s + "#" + rev

        # LPS array
        lps = [0] * len(combined)

        length = 0
        i = 1

        # Build LPS
        while i < len(combined):

            if combined[i] == combined[length]:

                length += 1
                lps[i] = length
                i += 1

            else:

                if length != 0:
                    length = lps[length - 1]

                else:
                    lps[i] = 0
                    i += 1

        # Longest palindromic prefix
        longest_palindrome = lps[-1]

        # Remaining part
        remaining = s[longest_palindrome:]

        # Reverse remaining part
        add = remaining[::-1]

        # Add it to the front
        return add + s