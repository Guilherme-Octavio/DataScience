from math import pow, factorial

def poisson(x,lam):
    return  pow(2.71828,-lam) *  pow(lam,x) / factorial(x)

#O Número de Acidentes de Carros que ocorrem por dia é de 2 acidentes. Qual a probabilidade de ocorrem 3 em um determinado dia?
print(poisson(3,2))







