def isSameAfterReversals(num: int) -> bool:
    # If num == 0 return True
    if num == 0: 
        return True
    
    # If num has a 0 at index -1 return False
    if str(num)[-1] == '0':
        return False
    
    return True 

test_cases = [526, 1800, 0, 4560, 304]

for i in range(len(test_cases)):
    print(f'{i}: {test_cases[i]}')
    print(isSameAfterReversals(test_cases[i]))
    print()