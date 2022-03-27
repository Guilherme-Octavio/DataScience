#Prof. Fernando Amaral
#2 alistamento
from datetime import date
anonascimento = int(input("Informe o ano de seu nacimento: "))
anoatual = float(date.today().year)
if anoatual-anonascimento > 18:
    print("Deve se alistar!")
else:
    print("Não deve se alistar!")

