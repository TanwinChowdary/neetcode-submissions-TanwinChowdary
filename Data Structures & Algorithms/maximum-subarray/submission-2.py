class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        local_sum = nums[0]
        for i in range (1, len(nums)):
            local_sum = max(local_sum + nums[i], nums[i])
            max_sum = max(max_sum, local_sum)
        return max_sum        
        