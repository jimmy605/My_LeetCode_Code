def isSubsequence(s: str, t: str) -> bool:
    s_list = list(s)

    for char in t:
        if s_list:
            if s_list[0] == char:
                s_list.pop(0)
        else:
            break 

    if len(s_list) == 0:
        return True 
    else:
        return False 

print(isSubsequence('abc', 'ahbgdc'))