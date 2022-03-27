#Professor Fernando Amaral
#5 Percentuais
total =  input("Informe o total de alunos: ")
total = int(total)
masculino =  input("Informe o total de alunos do sexo masculino: ")
masculino = int(masculino)
print("Percentual de alunos do sexo masculino: ",masculino * 100 / total )
print("Percentual de alunos do sexo feminino: ", (total  - masculino) * 100 / total)



