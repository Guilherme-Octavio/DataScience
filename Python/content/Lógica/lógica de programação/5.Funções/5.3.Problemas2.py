#Prof. Fernando Amaral
#2 Impressão de Intervalo

def impressao(int1,int2):
    for x in range(int1, int2+1):
        print(x)
    for int2 in range(int2,int1-1, -1):
        print(int2)


int1 = int(input("Informe o primeiro valor: "))
int2 = int(input("Informe o segundo valor: "))
impressao(int1,int2)

















