def titleToNumber(columnTitle: str) -> int:
    alphabet = {}
    column_number = 0

    for idx, letter in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
        alphabet[letter] = idx + 1

    for idx, letter in enumerate(columnTitle[::-1]):
        if idx == 0:
            column_number += alphabet[letter]
        else:
            column_number += (26 ** idx * alphabet[letter])

    return column_number

print(titleToNumber('ZY'))
print(titleToNumber('AB'))
print(titleToNumber('FXSHRXW')) #2147483647