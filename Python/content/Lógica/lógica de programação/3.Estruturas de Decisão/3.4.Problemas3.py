#Professor Fernando Amaral
#3 Habilitação para vaga
idade = int(input("Informe a Idade: "))
atividade = float(input("Informe o tempo de atividade profissional: "))
if (idade < 70) or (atividade>=25) or (idade >= 70 and atividade>=30):
    print("Habilitado!")
else:
    print("Não Habilitado")

#Testes
#70 de idade e outro valor qualuqer, habilitado
#24 anos de atividade profissional e outro valor qualquer, habilitado
#73 anos e 30 anos, habilitado (3º condição)
#72 e 22, não habilitado




    
    
