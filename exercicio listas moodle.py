lista = []

# adicionando elementos a lista

# append para adicionar elemento no final da lista
# insert(posicao,valor) para adicionar em posicao especifica

lista.append("A")  # append adiciona o elemento no final da lista
lista.insert(1, "B")  # adicionando elemento "B" na posicao 1
lista.append(12)  # adicionando o elemento 12 na ultima posicao

# removendo elementos da lista

# lista.pop() = remove o ultimo elemento da lista
# del lista[2] = removendo o elemento na posicao 2
# lista.remove("12") = removendo o elemento especifico contido na lista
lista.pop()


# excluindo elemento "A"

# lista.remove("A")
# del lista[0]
del lista[0]

print(lista)
