class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        comp_st = set()
        for i in range(len(nums)):
            if nums[i] in comp_st:
                return True
            else:
                comp_st.add(nums[i])
        return False
         