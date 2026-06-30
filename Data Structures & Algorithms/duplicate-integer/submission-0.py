class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        flag = False 
        nums = sorted(nums)
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                flag = True 
                break
        return flag