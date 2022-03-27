"""
Python

* Estudo introdutorio!
* Módulos e Pacotes específicos serão estudados durante o curso

Criado no final dos anos 80
Simple, facil e rápido aprendizado
menos código
sensivel a Maiúscula e minuscula

Curso usa a versão 3.X



"""
"""
Listas

* Vetor de valores
* Dados não precisam ser do mesmo tipo

"""

lst =[1,2,3,4]
lst2 = [1,2,3,"4", True]
lst3 = [1,2,[1,2,3,"4"], "a"]
lst4 = list(range(0,10)) # preenche de 0 a 10

# Acessando os elementos da lista || 0 == ao primeiro item 

lst[0]

# Numero de elemento em uma lista 

len(lst)

"""
Conjunto de Variaveis --- Dicionários Sets Tuplas
"""

"""
Dicionários

* Conjunto de chave/valor associados
* Declarados por chaves e separados por dois pontos(:)

ex. 
Preços = {'lapis': 10.0, 'Bolacha': 7.7, 'Caneta': 6.5}

No primeiro item o lapis é a chave e o valor é 10.0

"""
"""
Sets

* Conjunto não ordenado e não repetido de elementos

ex.
Animais = {'gato', 'cachorro', 'cavalo'}

Se você colocar 2 valores iguais será atribuida apenas uma

"""
"""
Tuplas

* Tuplas são listas que não podem ser alteradas

ex.

tp1 = (1,2,3,4,5,6)

comparando com JS, isso é uma const

"""
"""
Bibliotecas --- Numpy pandas

"""
"""
Numpy

* Computação Cientifica: Facilita operações matemáticas avançadas e outros tipos de operações em muitos dados
* Objetivo de Matiz Multidimensional
* Variedade de rotinas para operações rápidas em matrizes
* Os arrays Numpy têm um tamanho fixo na criação, ao contrariodas listas Python (Que o tamanho é dinamico)
* Os elementos em uma matriz Numpy devem ser todos do mesmo tipo de dados e, portanto, terão o mesmo tamanho na memória

"""
import numpy as np

# cria uma matriz unidimensional
a = np.array([12,34,26,18,10])
print(a)
print(a.dtype) # Mostra o tipo da variavel

"""
Pandas 
# Data Frame -- manipulaççao de dados #
# Series -- dados em séries #

Code ex.
"""
import pandas as pd

dados = pd.read_csv('nomeArquivo.csv')

"""
Módulos e Pacotes


"""