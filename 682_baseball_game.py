class Solution:
    def calPoints(self, ops):
        stack = []
        
        for op in ops:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'D':
                stack.append(stack[-1] * 2)
            elif op == 'C':
                stack.pop()
            else:
                stack.append(int(op))
        
        return sum(stack)

test = Solution()
print(test.calPoints(["5","2","C","D","+"]))
print(test.calPoints(["5","-2","4","C","D","9","+","+"]))
print(test.calPoints(['1']))
print(test.calPoints(["84","C","-87","D","D","15","C","-76","-28","-65","26","-49","+","+","-56","-82","+","+","-66","31"])) #-1427