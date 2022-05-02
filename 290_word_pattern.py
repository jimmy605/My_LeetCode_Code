class Solution:
    def wordPattern(self, pattern, s):
        data = {}
        pattern = list(pattern)
        s = s.split()
        
        if len(pattern) != len(s):
            return False 
        
        for i, p in enumerate(pattern):
            if p not in data:
                data[p] = s[i]
            elif p in data:
                if data[p] != s[i]:
                    return False 
        
        if list(data.values()).count(s[i]) > 1:
            return False 
        return True

test = Solution()
print(test.wordPattern('abba', 'dog cat cat dog'))
