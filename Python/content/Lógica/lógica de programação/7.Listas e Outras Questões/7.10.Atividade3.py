from math import sqrt

lista = list(range(0,5))


for n in range(0, 5):
    print("Informe o número da posição ", n+1, " da primeira lista")
    lista[n] = float(input())

for n in range(0, 5):
    print("Raiz quadrada: "sqrt(lista[n]))
    if sqrt(lista[n]) % 1 == 0 :
        print("Raiz quadrada é um valor inteiro")
    else:
        print("Raiz quadrada não é um valor inteiro")

