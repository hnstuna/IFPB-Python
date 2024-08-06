idade = int(input())

if idade < 5:
    print("Idade invalida.")
elif 4.9 < idade < 7.1:
    print("Infantil A")
elif 7.9 < idade < 10.1:
    print("Infantil B")
elif 10.9 < idade < 13.1:
    print("Juvenil A")
elif 13.9 < idade < 17.1:
    print("Juvenil B")
elif 17.9 < idade < 40.1:
    print("Adulto")
elif idade > 40.9:
    print("Master")
