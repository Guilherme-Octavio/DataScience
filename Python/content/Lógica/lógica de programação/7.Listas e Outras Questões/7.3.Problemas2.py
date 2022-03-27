#professor Fernando Amaral

lista = list(range(1,11))
print(lista)

#entrada de dados
for n in range(0, 10):
    print("Informe o número da posição ", n+1)
    lista[n] = int(input())


#forma 1, ordenar e exibir primeiro e ultimo elemento
lista2 = sorted(lista)
print("O maior valor é: " ,  lista2[9])
print("O Menor valor é: ", lista2[0])


#forma dois, max e min  
print("O maior valor é: " ,  max(lista))
print("O Menor valor é: ", min(lista))

