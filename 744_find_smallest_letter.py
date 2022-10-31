import string 

class Solution:
    def nextGreatestLetter(self, letters, target):
        for c in letters:
            if c > target:
                return c
        return letters[0]

test = Solution()
print(test.nextGreatestLetter(["c","f","j"], 'a')) #"c"
print(test.nextGreatestLetter(["c","f","j"], 'c')) # "f"
print(test.nextGreatestLetter(["c","f","j"], 'd')) # "f"
print(test.nextGreatestLetter(["c","f","j"], 'a')) # "c"
print(test.nextGreatestLetter(["c","f","j"], 'j'))
print(test.nextGreatestLetter(["c","f","j"], 'k'))
print(test.nextGreatestLetter(["e","e","e","e","e","e","n","n","n","n"], 'e'))