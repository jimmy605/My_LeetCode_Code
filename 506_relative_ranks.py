class Solution:
    def findRelativeRanks(self, score):
        output = {}
        sorted_places = sorted(score, reverse=True)
        output_list = []
        count = 4
        
        for i in range(len(score)):
            if i > 2:
                output[sorted_places[i]] = str(str(count))
                count += 1
            elif i == 0:
                output[sorted_places[i]] = 'Gold Medal'
            elif i == 1:
                output[sorted_places[i]] = 'Silver Medal'
            else:
                output[sorted_places[i]] = 'Bronze Medal'
        
        for i in score:
            output_list.append(output[i])
        
        return output_list

test = Solution()
print(test.findRelativeRanks([i for i in range(5, 0, -1)]))