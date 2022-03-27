#Professor Fernando Amaral
#5 Impostos
total =  float(input("Informe o valor total da manutenção: "))
issqn =  float(input("Informe o percentual de impostos sobre serviços: "))
icms =  float(input("Informe o percentual de impostos sobre circulação de produtos: "))

totalissqn = total * (issqn/100)
totalicms =total * (icms/100)

print("O total de ISSQN é de  ", totalissqn)
print("O total de ICMS é de  ", totalicms)
print("O valor restante retirado os impostos é de   ",total -  totalissqn - totalicms)     




