figura = input()

if figura == "retangulo":
    base = int(input())
    altura = int(input())
    A = base*altura
    print("{:.2f}".format(A))

elif figura == "triangulo":
    base = int(input())
    altura = int(input())
    A = base*altura/2
    print("{:.2f}".format(A))

elif figura == "trapezio":
    basemaior = int(input())
    basemenor = int(input())
    altura = int(input())
    A = ((basemaior+basemenor)/2)*altura
    print("{:.2f}".format(A))

elif figura == "circulo":
    raio = int(input())
    A = 3.1415*raio**2
    print("{:.2f}".format(A))

else:
    print("Figura invalida.")
