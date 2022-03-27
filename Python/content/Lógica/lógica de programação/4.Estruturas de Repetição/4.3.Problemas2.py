#Professor Fernando Amaral
#2 Impressão de intervalo
valido = False
while valido==False:
    int1 = int(input("Informe o primeiro valor: "))
    int2 = int(input("Informe o segundo valor: "))
    #precisamos que as condições sejam falsas
    if int1>0 and int2>0 and int1<int2:
        valido = True

#range(inicio, parada, incremento)
#não inclui o valor de parada por isso + 1 e -1
#indexados em zero

#x será inicializado automáticamente
#step é opcional, se é 1 não precisa informar
for x in range(int1, int2+1):
    print(x)

#aqui precisamos usar int2
#step -1 vai fazer o efeito decrecente
for int2 in range(int2,int1-1, -1):
     print(int2)










