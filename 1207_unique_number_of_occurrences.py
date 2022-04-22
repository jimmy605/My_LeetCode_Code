import collections

class Solution:
    def uniqueOccurrences(self, arr):
        data = len(set(collections.Counter(arr).values()))
        L_set = len(set(arr))
        
        return data == L_set


test = Solution()
print(test.uniqueOccurrences([1,2,2,1,1,3]))