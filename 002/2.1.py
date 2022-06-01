
l = list(map(int, input('Enter the list: ').split()))
def multiplication():
    new_l = []
    left = 0
    while left < (len(l) + 1) // 2:
        right = (left + 1) * -1
        new_l.append(l[left] * l[right])
        left += 1
    return new_l
print(multiplication())
