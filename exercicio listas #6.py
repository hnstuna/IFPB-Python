nAlunos = int(input())
listaF = []

for i in range(1, nAlunos+1):
    aluno = input()
    pont = int(input())
    if pont >= 80:
        listaF.append(aluno)
        listaF.append(pont)
print(listaF)

#  para printar em sequencia
'''
for i in listaF:
    print(i)
'''
