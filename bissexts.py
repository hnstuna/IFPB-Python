n1 = int(input())
n2 = int(input())

if n2 - n1 < 4:
    print('-1')
if n1 % 2 == 0: # eh par
    for i in range(n1, n2, 4):
        print(i)
else: # eh impar
    for i in range(n1-1, n2-1, 4):
        print(i)
