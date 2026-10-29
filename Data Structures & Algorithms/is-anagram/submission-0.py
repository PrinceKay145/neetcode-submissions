class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #check the length 
        return "".join(sorted(s)) == "".join(sorted(t))
        