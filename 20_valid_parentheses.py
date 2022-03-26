def isValid(s: str) -> bool:
    string_stack = []
    dict_values = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    
    for c in s:
        if c in dict_values.values():
            string_stack.append(c)
        if c in dict_values.keys():
            if len(string_stack) == 0:
                return False
            elif dict_values[c] == string_stack.pop():
                continue
            else:
                return False
    
    return len(string_stack) == 0


print(isValid('()'))
print(isValid('()[]{}'))
print(isValid('(]')) 