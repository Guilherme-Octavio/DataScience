#Professor Fernando Amaral

lista = ["Fernando", "José", "MARCOS", "ANA", "MARIA", "valentina", "Irene", "Lucas", "Adão", "Eva"]
print("Informe um nome para Localização ")
nome = input()


encontrado = False
for n in range(0, len(lista)):
    print(lista[n])
    if lista[n].lower() == nome.lower():
        encontrado = True

if encontrado==False:
    print("Nome não encontrado")
else:
    print("Nome encontrado")
		
