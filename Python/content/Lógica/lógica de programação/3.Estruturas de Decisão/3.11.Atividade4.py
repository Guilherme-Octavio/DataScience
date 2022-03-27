#Prof. Fernando Amaral
#4 Habilitação pra vaga
idade = int(input("Informe a Idade: "))
print("Informe a escolaridade: ")
print("1 – ensino fundamental")
print("2 – ensino médio")
print("3 – ensino superior ")
escolaridade = float(input())

if (escolaridade==3) or (escolaridade==2 and idade>60):
    print("Habilitado!")
else:
    print("Não Habilitado!")

