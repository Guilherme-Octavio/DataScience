#Prof. Fernando Amaral
#1 Conversão de temperatura

def converte(tipo,temp):
    if tipo==1:
        temp = (temp * 9/5) + 32
    else:
        temp = ((temp - 32)* 5) /9
    return temp

tp = int(input("Informe o tipo de conversão 1 para Celsius para Fahrenheit e 2 para Fahrenheit para Celsius : "))
temperatura = int(input("Informe a temperatura para converter: "))

print("O resultado é: ", converte(tp,temperatura ))



















