# 1 = Felix ficou com o pedaço que vale 100
# 2 = Marzia ficou com o pedaço que vale 100
# 0 = O valor da nota se perdeu
# Marzia lado direito da nota
# Felix lado esquerdo da nota

B = int(input())
T = int(input())
area = B*T

if area == 6300:
    print(0)
elif area < 5600:
    print(2)
elif area > 5600:
    print(1)
