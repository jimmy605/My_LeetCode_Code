def findAnagrams(s: str, p: str) -> List[int]:
    s_len = len(s)
    p_len = len(p)
    
    # Func that checks for anagram
    def anagram(letters, ana_letters=p):
        
    
    # Iterate through s and check if any of the characters are of p
    for char, idx in enumerate(s):
        if char in p and idx < (s_len - p_len):
            anagram(s[idx: idx + p_len])
    