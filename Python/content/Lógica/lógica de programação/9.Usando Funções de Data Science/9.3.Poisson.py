from scipy.stats import poisson

#O Número de Acidentes de Carros que ocorrem por dia é de 2 acidentes. Qual a probabilidade de ocorrem 3 em um determinado dia?
print(poisson.pmf(3, 2))

