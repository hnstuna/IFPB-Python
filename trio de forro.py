arreca = 0
qntd = 0
recusadoData = 0
recusadoDistnc = 0
show0110 = 0
show1120 = 0
show2130 = 0
valor = 0

while True:
    dist = int(input())
    if dist < 0:
        break

    if qntd > 6:
        qntd = 6

    if dist <= 50 and dist != 1 and dist != 2 and dist != 3:
        valor = dist * 5
        arreca = arreca + valor

    if 50 < dist <= 100 and dist != 1 and dist != 2 and dist != 3:
        valor = dist * 6.50
        arreca = arreca + valor

    if 100 < dist < 500 and dist != 1 and dist != 2 and dist != 3:
        valor = dist * 10
        arreca = arreca + valor

    if dist > 500:
        recusadoDistnc = recusadoDistnc + 1

    if dist == 1:
        show0110 = show0110 + 1
        if show0110 > 6:
            show0110 = 6
            arreca = arreca - valor
            recusadoData = recusadoData + 1


    if dist == 2:
        show1120 = show1120 + 1
        if show1120 > 6:
            show1120 = 6
            arreca = arreca - valor
            recusadoData = recusadoData + 1

    if dist == 3:
        show2130 = show2130 + 1
        if show2130 > 6:
            show2130 = 6
            arreca = arreca - valor
            recusadoData = recusadoData + 1

qntd = show0110 + show1120 + show2130

valorfinal = arreca+qntd*1000



if show0110 == 0 and show1120 == 0 and show2130 == 0:
    print("Arrecadado: R$", "{:.2f}".format(valorfinal))
    print("Quantidade de Shows:", qntd)
    print("Shows Recusados por Data:", recusadoData)
    print("Shows Recusados por Distância:", recusadoDistnc)
else:
    print("Arrecadado: R$", "{:.2f}".format(valorfinal))
    print("Quantidade de Shows:", qntd)
    print("Shows Recusados por Data:", recusadoData)
    print("Shows Recusados por Distância:", recusadoDistnc)
    print("Shows de 01 a 10/06:", show0110, "festa(s)")
    print("Shows de 11 a 20/06:", show1120, "festa(s)")
    print("Shows de 21 a 30/06:", show2130, "festa(s)")
