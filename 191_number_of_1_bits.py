def hammingWeight(n):
    return bin(n).count('1')


print(hammingWeight(11111111111111111111111111111101))