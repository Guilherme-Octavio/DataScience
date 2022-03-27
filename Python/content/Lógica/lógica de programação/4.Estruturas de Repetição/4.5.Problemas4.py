#Professor Fernando Amaral
#4 Tabuada II
impressao = True
while impressao==True:
    tab = int(input("Informe tabuada que quer imprimir: "))
    for n in range(1, 11):
        print(n, " x ", tab, " = " , n * tab)
    resp = input("Deseja imprimir nova tabuada? Informe S para sim e N para não: ")
    if resp.upper()=="N":
        impressao = False













