def findContentChildren(g, s):
    satisfied_children = 0
    cookies = {}
    
    for i in s:
        if i in cookies:
            cookies[i] += 1
        else:
            cookies[i] = 1
    
    for child in sorted(g):
        if child in cookies and cookies[child] > 0:
            cookies[child] -= child 
    
    return satisfied_children

print(findContentChildren([1,2], [1,2,3]))
print(findContentChildren([1,2,3], [3]))
print(findContentChildren([1,2,3], [1,1]))