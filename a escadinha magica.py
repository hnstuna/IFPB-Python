n = int(input())

for j in range(n+1):
    for i in range(1, j+1):
        if i != j:
            print(i, end=' ')
        else:
            print(i)
