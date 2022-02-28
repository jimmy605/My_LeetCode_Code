
def countWords(words1, words2):
    count = 0
    
    def array_to_dict(array):
        """Returns a dict with keys being the word and value being the number of occurences of the word in the array."""
        output = {}
        for word in array:
            if word not in output:
                output[word] = 1
            else:
                output[word] += 1
        
        return output
    
    word1_dict = array_to_dict(words1)
    word2_dict = array_to_dict(words2)
    
    for word, occurences in word1_dict.items():
        if word not in word2_dict:
            continue 
        if occurences == 1 and word2_dict[word] == 1:
            count += 1
    
    return count 

print(countWords(["leetcode","is","amazing","as","is"], ["amazing","leetcode","is"]))