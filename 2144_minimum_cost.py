def minimumCost(cost) -> int:
    if len(cost) <= 2:
        return sum(cost)
    
    total_cost = []
    cost.sort()
    
    while cost:
        if len(cost) >= 3:
            total_cost.append(cost.pop())
            total_cost.append(cost.pop())
            cost.pop()
        
        elif len(cost) == 2:
            total_cost.append(cost.pop())
            total_cost.append(cost.pop())
        
        elif len(cost) == 1:
            total_cost.append(cost.pop())
        
        else:
            break 
    
    return sum(total_cost)


print(minimumCost([5,5]))
print(minimumCost([1,2,3]))
print(minimumCost([6,5,7,9,2,2]))
print(minimumCost([3,3,3,1]))