lista = list(range(0,5))

for n in range(0, 5):
    print("Informe o número da posição ", n+1)
    lista[n] = input()

for n in range(0, 5):
    nometmp = lista[n][0].upper() + lista[n][ 1 : len(lista[n])   ].lower()
    print("Nome na posição ", n+1, lista[n])
 
