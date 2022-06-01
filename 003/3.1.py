
l = list(map(float, input('Enter the list: ').split()))
l = [round(i % 1, 2) for i in l if int((i*100) % 100) > 0]
res = max(l) - min(l)
print(max(l), min(l))
print(res)