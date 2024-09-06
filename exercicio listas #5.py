idades = []
cont = 0

while True:
    idade = int(input())
    if idade < 0:
        break
    else:
        idades.append(idade)
        cont = cont + 1

menorIdade = min(idades)  # funcao min() "pega" o menor elemento da lista
maiorIdade = max(idades)  # funcao max() mesma funcao porem o maior da lista
somaIdade = sum(idades)  # soma os elementos de uma lista
mediaIdade = somaIdade / cont

for i in idades:
    print(i, "anos")
print("Menor idade:", menorIdade, "anos")
print("Maior idade:", maiorIdade, "anos")
print("Idade media da turma:", "{:.0f}".format(mediaIdade), "anos")
