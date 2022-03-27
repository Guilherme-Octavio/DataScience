#Professor Fernando Amaral
lista1 = list(range(1,6))
lista2 = list(range(1,6))

#entrada de dados
for n in range(0, 5):
    print("Informe o número da posição ", n+1, " da primeira lista")
    lista1[n] = int(input())

for n in range(0, 5):
    print("Informe o número da posição ", n+1, " da segunda lista lista")
    lista2[n] = int(input())


for n in range(0, 5):
    if lista1[n] == lista2[n]:
        print("Coincidência do valor ", lista1[n], " na posição ", n+1)
    else:
        print("Valores ", lista1[n], " e ", lista2[n], " diferentes na posição ", n+1) 


