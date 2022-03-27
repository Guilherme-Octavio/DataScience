#Prof. Fernando Amaral
#1 Entrar na Faculdade
idade = int(input("Informe a Idade: "))
nota = float(input("Informe a nota do Enem: "))
brasileiro = input("Digite \"S\" se é brasileiro ou \"N\" caso não seja: ")
brasileiro = brasileiro.upper()
if idade<25 and nota>=70 and brasileiro=="S":
    print("Aprovado!")
else:
    print("Reprovado!")

