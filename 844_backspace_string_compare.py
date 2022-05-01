class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def data(string):
            ans = []
            
            for char in string:
                if char != '#':
                    ans.append(char)
                elif ans:
                    ans.pop()
            
            return ''.join(ans)
        
        return data(s) == data(t)