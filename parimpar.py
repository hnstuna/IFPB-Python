n = int(input())
m = int(input())

if n % 2 == 0: # eh par
    for i in range(n+1, m, 2):
        print(i)
else: # nao eh par
    for j in range(n, m+1, 2):
        print(j)
