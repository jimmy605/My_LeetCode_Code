from itertools import permutations

def findEvenNumbers(digits: list[int]) -> list[int]:
    if sum(digits) == 0:
        return []

    new_digits = []
    
    for i in digits:
        if i not in new_digits:
            new_digits.append(i)
        elif i in new_digits and new_digits.count(i) < 3:
            new_digits.append(i)
        
    print(new_digits)
    
    output = []
    perms = permutations(new_digits, 3) 
    
    for i in list(perms):
        if i[0] == 0:
            continue
        join_list = int(''.join([str(j) for j in i]))
        if join_list % 2 == 0:
            output.append(join_list)

    return sorted(set(output))
    
print(findEvenNumbers([2,1,3,0]))
print(findEvenNumbers([3,6,4,7,1,2,7,4,3,8,4,8,1,8,1,8,6,7,8,2,8,9,3,9,8,5,9,2,4,4,7,5,9,1,9,7,5,7,1,9,3,7,4,1,0,4,1,2,5,6,7,9,6,3,8,1,0,4,7,0,3,7,3,4,1,0,6,3,7,9,5,0,5,7,7,4,7,5,5,1,1,2,5,9,4,5,7,7,4,4,3,4,6,2,7,8,5,9,4,5]))