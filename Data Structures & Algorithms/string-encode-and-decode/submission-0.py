class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded = []
        for s in strs:
            encoded.append(f"{len(s)}#{s}")
        return "".join(encoded)
        
    def decode(self, s: str) -> List[str]:
        solve = []
        i = 0
        while i < len(s):
            # find the '#' that separates length from string
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            start = j + 1
            solve.append(s[start:start + length])
            i = start + length
        return solve    

