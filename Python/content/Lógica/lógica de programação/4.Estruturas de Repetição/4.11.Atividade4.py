#professor Fernando Amaral
# 4 validação de valores

valido = False
while valido==False:
    val1 = int(input("Informe o primeiro valor: "))
    val2 = int(input("Informe o segundo valor: "))
    if val1>10 and val2>10*val1:
        valido = True
    else:
        print("Valores inválidos!")

print("Produto: ", val1 * val2)









