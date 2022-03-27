lista = list(range(0,5))
anterior = 0
invalido = True

for n in range(0, 5):
    print("Informe o número da posição ", n+1)
    lista[n] = int(input())
    while lista[n] <= anterior:
               print("Valor ", lista[n], " inválido, tente novamente")
               lista[n] = int(input())    
    anterior = lista[n]
           


    
 

