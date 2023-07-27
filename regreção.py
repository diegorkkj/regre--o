x = "n"

while x !="y":
    b = int(input("Digite um numero para realizar a contagem Regressiva: "))
    
    while b >= 0:
        print(b)
        b = b-1
        if b < -1:
            while b < 0:
                print(b)
                b = b+1

    x = input("Deseja sair? \n y = SIM \n n = NÃO \n")
    if x == "Y" or x == "sim":
        x = "y"
    elif x == "N" or x == "não":
        x = "n"