#Professor Fernando Amaral
from statistics import mean

lista = list(range(1,11))


#entrada de dados
for n in range(0, 10):
    print("Informe o número da posição ", n+1)
    lista[n] = int(input())
    while lista[n] <=0:
        print("Entrada Inválida, por favor repita!")
        lista[n] = int(input())


#calculo da média manual
soma = 0
for n in range(0, 10):
    soma += lista[n]

print("Média calculada \"manualmente\" igual a: ", soma / 10)    


#calculo da média usando função
print("Média calculada \"por função\" igual a: ",mean(lista))
