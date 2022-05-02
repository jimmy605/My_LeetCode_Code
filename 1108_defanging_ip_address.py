class Solution:
    def defangIPaddr(self, address):
        output = ''
        
        for i in address:
            if i == '.':
                output += '[.]'
            else:
                output += i
        
        return output