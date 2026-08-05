class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        maxProduct = nums[0]
        minProduct = nums[0]
        ans = nums[0]

        for i in range(1, len(nums)):

            if nums[i] < 0:
                maxProduct, minProduct = minProduct, maxProduct

            maxProduct = max(nums[i], nums[i] * maxProduct)
            minProduct = min(nums[i], nums[i] * minProduct)

            ans = max(ans, maxProduct)

        return ans