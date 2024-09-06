Arrecadado = 0
Dia1 = 0
Dia2 = 0
Dia3 = 0
Shows = 0
RecusadoDistancia = 0
RecusadoData = 0
SomarDepois = 0
Valor = 0

while True:
    Distancia = int(input())

    if Distancia < 0:
        break

    elif Distancia == 0:
        SomarDepois += 1

    elif Distancia > 500:
        RecusadoDistancia += 1
        continue

    elif Distancia <= 50 and Distancia > 0:
        Valor = Distancia * 5
        Arrecadado += Valor

    elif Distancia > 50 and Distancia <= 100:
        Valor = Distancia * 6.50
        Arrecadado += Valor

    elif Distancia > 100 and Distancia<= 500:
        Valor = Distancia * 10
        Arrecadado += Valor

    Data = int(input())

    if Data == 1:
        if Dia1 < 6:
            Dia1 += 1


        else:
            RecusadoData += 1
            Arrecadado = Arrecadado - Valor
            continue

    elif Data == 2:
        if Dia2 < 6:
            Dia2 += 1


        else:
            RecusadoData += 1
            Arrecadado = Arrecadado - Valor
            continue

    elif Data == 3:
        if Dia3 < 6:
            Dia3 += 1


        else:
            RecusadoData += 1
            Arrecadado = Arrecadado - Valor
            continue

    Shows += 1

Arrecadado = Arrecadado + (Shows * 1000)

if Shows != 0:
    print('Arrecadado: R$ %.2f'%(Arrecadado))
    print('Quantidade de Shows: %i'%(Shows))
    print('Shows Recusados por Data: %i'%(RecusadoData))
    print('Shows Recusados por Distância: %i'%(RecusadoDistancia))
    print('Shows de 01 a 10/06: %i festa(s)'%(Dia1))
    print('Shows de 11 a 20/06: %i festa(s)'%(Dia2))
    print('Shows de 21 a 30/06: %i festa(s)'%(Dia3))

else:
    print('Arrecadado: R$ %.2f'%(Arrecadado))
    print('Quantidade de Shows: %i'%(Shows))
    print('Shows Recusados por Data: %i'%(RecusadoData))
    print('Shows Recusados por Distância: %i'%(RecusadoDistancia))
