def minimumSum(num: int) -> int:
    sorted_digits = sorted(str(num))
    total = 0

    if num == 0:
        return total

    for i in range(2):
        total += int(''.join([str(sorted_digits[i]), str(sorted_digits[i + 2])]))

    return total

print(minimumSum(2932))