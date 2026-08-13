class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        last = {}

        # Store last occurrence of every character
        for i in range(len(s)):
            last[s[i]] = i

        ans = []
        start = 0
        end = 0

        # Traverse the string
        for i in range(len(s)):
            end = max(end, last[s[i]])

            # Partition can end here
            if i == end:
                ans.append(end - start + 1)
                start = i + 1

        return ans