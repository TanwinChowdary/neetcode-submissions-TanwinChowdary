class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        check_map = {}
        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in check_map:
                return [check_map[diff],i]
            check_map[n] = i
            


        