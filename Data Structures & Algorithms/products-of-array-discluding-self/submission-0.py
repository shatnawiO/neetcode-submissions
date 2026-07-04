class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)

        for num in range(1,len(nums)):
            prefix[num] = prefix[num-1]*nums[num-1]

        for num1 in range(len(nums)-2,-1,-1):
            suffix[num1] = suffix[num1+1] * nums[num1+1]
                
        solve = []
        for i in range(len(nums)):
            solve.append(suffix[i]*prefix[i])
        return solve    

        

        