idade = int(input())

if idade >= 18:
    print("Voce ja pode tirar habilitacao!")
    print("Voce tem direito a habilitacao ha", idade-18, "ano(s)")
else:
    if idade < 18:
        print("Voce precisa esperar mais", 18-idade, "ano(s)!")
