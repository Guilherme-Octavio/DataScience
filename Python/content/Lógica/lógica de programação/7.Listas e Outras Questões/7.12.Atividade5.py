lista = list(range(0,5))

invalido = False

for n in range(0, 5):
    print("Informe o número da posição ", n+1)
    lista[n] = int(input())
    while invalido==True:
        if lista[n] <=0:
            print("Valor inválido, tente novamente!")
            lista[n] = int(input())
        else:
            invalido = False


for n in range(0, 5):
    if lista[n] % 2 == 0:
        print("Número na posição ", n+1, " é igual a ", lista[n], " e é par.")
        
        

