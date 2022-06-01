n = int(input('Enter the number: '))
def DecimalToBinaryConverter(n, s = ''):
    while n > 0:
        s += str(n % 2)
        n //= 2
    return s[::-1]
print(DecimalToBinaryConverter(n))