class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        solve  = 1
        nums = sorted(nums)
        n = len(nums)
        if n == 0 :
            return 0
        count  = 1     
        for i in range(n-1):
            if nums[i]+1 == nums[i+1]:
                count+=1
            elif nums[i]+1 != nums[i+1]:
                if nums[i] == nums[i+1]:
                    continue 
                solve = max(count,solve)
                count = 1
        solve = max(count,solve)
        return  solve       
        