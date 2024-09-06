ano = int(input())
intervalo = int(input())
inicio = ano+intervalo

if intervalo == 0:
    print(ano, ano, ano)

else:
    for i in range(inicio, ano+intervalo*4, intervalo):
        print(i, end=' ')
