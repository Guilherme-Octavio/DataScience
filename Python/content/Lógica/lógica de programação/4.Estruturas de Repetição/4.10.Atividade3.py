#Professor Fernando Amaral
#3 Tabuada
tab = 1
while tab<11:
    print("--------------------")
    for n in range(1, 11):
        resp =  "|" +  str(n) +  " x " + str(tab) + " = " + str( n * tab )
        esp = "  " * (14 - len(resp)) + "|"
        print(resp + esp)
        if n==10:
            tab = tab + 1
            break
print("--------------------")










