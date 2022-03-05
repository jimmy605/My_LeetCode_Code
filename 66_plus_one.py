def plusOne(digits: int) -> int:
    add_one = int(''.join([str(i) for i in digits])) + 1
    
    return [int(i) for i in str(add_one)]

print(plusOne([1,2,3]))