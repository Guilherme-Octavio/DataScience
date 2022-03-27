#Professor Fernando Amaral
#5 Calculadora de média
tab = int(input("Quantos números serão calculados? "))
soma = 0
for tab in range(1, tab+1):
    texto = "Informe o " + str(tab) + "º número: " 
    soma = soma + int(input(texto))
print("A média é igual a : ", soma / tab)












