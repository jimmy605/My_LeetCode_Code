def isPalindrome(s: str) -> bool:
    if s in ['', ' ']:
        return True 
    
    just_letters = []
    for e in s:
        if e.isalpha():
            just_letters.append(e.lower())
        if e.isdigit():
            just_letters.append(e)
    
    return just_letters == just_letters[::-1]


print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("0P"))
