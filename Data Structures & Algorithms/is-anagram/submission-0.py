class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic_t = {}
        dic_s = {}
        for char in s:
            if char in dic_s:
                dic_s[char]+=1
            else:
                dic_s[char] = 1        

        for charr in t :
            if charr in dic_t:
                dic_t[charr]+=1
            else:
                dic_t[charr] = 1

        if dic_s == dic_t:
            return True 
        return False            
        