class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxsum = nums[0]
        currSum = 0
        for num in nums:
            if currSum<0:
                currSum = 0
            currSum += num
            maxsum = max(maxsum, currSum)
        return maxsum        