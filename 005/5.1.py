
def fibo(n):
    if n >= 0:
       x = [0, 1]
       for i in range(2, n+1):
           x.append(x[i-1] + x[i-2])
       return x[n]
    else:
       n=-(n-1)
       x = [1,0]
       for j in range(2, n+1):
           x.append(x[j-2] - x[j-1])
       x.reverse()
    return x[0]

for k in range(-10,11):
   print(fibo(k), end=' ')


