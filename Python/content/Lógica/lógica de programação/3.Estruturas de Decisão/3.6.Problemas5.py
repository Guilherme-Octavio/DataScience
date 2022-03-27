#Professor Fernando Amaral    
#5 Descontos
quantidade = int(input("Informe a quantidade de produtos: "))
total = float(input("Informe valor total da compra: "))
#desconto = 0 caso seja comprado apenas 1 produto
desconto = 0
if quantidade == 2:
    desconto = 0.02
elif quantidade> 2 and quantidade<=5:
    desconto = 0.05
elif quantidade>5 and quantidade<10:
    desconto = 0.1
elif quantidade >=10:
    desconto = 0.15

#não pode ter else se não vai dar desconto pra 1 produto

calcdesc = total - (total * desconto)

print("Valor Total da Compra: ", total)
print("Valor Total com Desconto: ", calcdesc)
print("Economia: ", total - calcdesc)




    
    
