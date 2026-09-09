class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}

        # Step 1: Count frequency of each character
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1

        # Step 2: Find the first character whose frequency is 1
        for i in range(len(s)):
            if freq[s[i]] == 1:
                return i

        # Step 3: No unique character found
        return -1