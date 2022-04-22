class Solution:
    def shortestDistance(self, wordsDict, word1, word2):
        data = {word1:[], word2:[]}
        
        for ind, word in enumerate(wordsDict):
            if word in data:
                data[word].append(ind+1)
        
        # Function that works out the smallest difference in numbers
        def smallest_difference(data, word1, word2):
            word1_list = data[word1]
            word2_list = data[word2]
            smallest = []
            
            for i in range(len(word1_list)):
                for j in range(len(word2_list)):
                    smallest.append(abs(word1_list[i] - word2_list[j]))
            
            # print(smallest)
            return sorted(smallest)[0]
        
        return smallest_difference(data, word1, word2)


test = Solution()
print(test.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], 'coding', 'practice'))
print(test.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "makes", 'coding'))