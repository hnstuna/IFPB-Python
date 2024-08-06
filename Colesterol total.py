valor = float(input())

if valor < 150:
    print("Colesterol total", valor, "mg/dl (DESEJAVEL)")
elif 150 <= valor <= 170:
    print("Colesterol total", valor, "mg/dl (LIMITROFE)")
elif valor > 170:
    print("Colesterol total", valor, "mg/dl (ALTO)")
