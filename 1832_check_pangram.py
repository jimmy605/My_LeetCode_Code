# from string import ascii_lowercase

class Solution:
    def checkIfPangram(self, sentence):
        # alphabet = list(ascii_lowercase)
        
        # for letter in sentence:
        #     if letter in alphabet:
        #         alphabet.remove(letter)
        
        # return True if alphabet == [] else False 
        letters = set()
        
        for letter in sentence:
            letters.add(letter)
        
        letters_length = len(list(letters))
        return True if letters_length == 26 else False 

test = Solution()
print(test.checkIfPangram("thequickbrownfoxjumpsoverthelazydog"))
print(test.checkIfPangram('leetcode'))