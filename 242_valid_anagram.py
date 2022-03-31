class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        return True if sorted(s) == sorted(t) else False 

test = Solution()
print(test.isAnagram('anagram', 'nagaram'))