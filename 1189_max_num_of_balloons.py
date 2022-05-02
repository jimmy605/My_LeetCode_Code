class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # If the text < len(balloon) return False
        L = len(text)
        if L < len('balloon'):
            return False 
        
        