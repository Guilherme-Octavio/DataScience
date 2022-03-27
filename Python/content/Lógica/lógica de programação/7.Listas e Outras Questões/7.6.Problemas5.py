
#Professor Fernando Amaral
from impressao import imprime
#arquivo impressao.py deve estar no mesmo diretório
valido = False
while valido == False:
    int1 = int( input("Informe o primeiro valor inteiro: "))
    int2 = int( input("Informe o segundo valor inteiro: "))
    if int2 <= int1:
        print("Valores inválidos! Tente novamente!")
    else:
        valido=True

imprime(int1,int2)
