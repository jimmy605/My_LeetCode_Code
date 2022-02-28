def isPowerOfTwo(self, n: int) -> bool:
    for i in range(32):
        calculation = 2 ** i
        if calculation == n:
            return True
        elif calculation > n:
            return False

print(isPowerOfTwo(4))
print(isPowerOfTwo(16))
print(isPowerOfTwo(166))
