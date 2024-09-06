maisNovo = 999
maisVelho = 1

for i in range(1,101):
    n = int(input())
    if n < maisNovo:
        maisNovo = n
    if n > maisVelho:
        maisVelho = n

print("mais novo:", maisNovo)
print("mais velho:", maisVelho)
