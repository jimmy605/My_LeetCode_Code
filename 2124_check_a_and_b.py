def checkString(s: str) -> bool:
    # Length of string
    l = len(s)
    
    # Change the string into a list
    s_list = list(s)
    
    # Find the index of the first b. Leave as False till proven it's in the string 
    first_b_index = -1
    
    # Check for b's index. Update first_b_index if it's in the string
    for i in range(l):
        if s[i] == 'b':
            first_b_index = i
            break 
    
    # If b not in the input or is the length of the list return True
    if first_b_index == -1 or first_b_index == (l - 1):
        return True 
    
    # Iterate through list starting at first b's index + 1
    for i in range(first_b_index + 1, l):
        # If any a's are found after the b return False
        if s_list[i] == 'a':
            return False
    
    return True 


test_cases = ['aaabbb', 'abab', 'bbb', 'a', 'b', 'aaa']

for i in range(len(test_cases)):
    print('testcase:', test_cases[i])
    print(checkString(test_cases[i]))
    print()