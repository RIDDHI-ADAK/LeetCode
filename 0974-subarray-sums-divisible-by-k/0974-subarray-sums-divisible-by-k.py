class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:

        prefix_sum = 0
        remainder_count = {0: 1}
        ans = 0

        for num in nums:

            prefix_sum += num

            remainder = prefix_sum % k

            ans += remainder_count.get(remainder, 0)

            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1

        return ans