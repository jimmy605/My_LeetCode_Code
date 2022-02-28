def canConstruct(ransomNote: str, magazine: str) -> bool:
    magazine_list = list(magazine)
    
    for char in list(ransomNote):
        if char in magazine_list:
            magazine_list.remove(char)
        else:
            return False
    
    return True 