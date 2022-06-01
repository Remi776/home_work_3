
l = list(map(int, input('Enter the list: ').split()))
def summ():
    res = 0
    for item in range(1, len(l)):
        if item % 2 != 0:
            res += l[item]
    return res
print(summ())