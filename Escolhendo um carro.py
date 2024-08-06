ei = input() #espaço interno (A)mplo ou (C)ompacto
pm = input() #porta malas (G)rande ou (P)equeno
vc = float(input()) #valor carro
mt = float(input()) #motor
cb = input() #cambio (A)utomático ou (M)anual

if ei == "C" or pm == "P":
    print("Não compre!")
else:
    if vc > 100000 and mt < 1.5 and cb == "M": #nenhum requisito
        print("Recomendo pensar melhor...")
    elif vc < 100000 and mt < 1.5 and cb == "M": #um requisito (valor)
        print("Pode ser uma opção.")
    elif vc > 100000 and mt > 1.5 and cb == "M": #um requisito (motor)
        print("Pode ser uma opção.")
    elif vc > 100000 and mt < 1.5 and cb == "A": #um requisito (cambio)
        print("Pode ser uma opção.")
    elif vc < 100000 and mt >= 1.5 and cb == "M": #2 requisito (valor/motor)
        print("Boa compra.")
    elif vc < 100000 and mt < 1.5 and cb == "A": #2 requisito (valor/cambio)
        print("Boa compra.")
    elif vc > 100000 and mt >= 1.5 and cb == "A": #2 requisito (motor/cambio)
        print("Boa compra.")
    else:
        print("Pode comprar!")
