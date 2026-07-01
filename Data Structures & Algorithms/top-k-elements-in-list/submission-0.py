class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        o = {}
        for num in nums:
            if num in o :
                o[num]+=1
            else:
                o[num]=1
        o = sorted(o.items(), key=lambda item: item[1],reverse = True) 
        solve = []
        for i in range(k):
            solve.append(o[i][0])    
        return solve
        