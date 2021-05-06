def soma(): #Função soma
    soma = eval(input("Digite na forma a + b + ... + n os valores que você quer somar\n"))
    print(soma)

def subtracao(): #Função subtração
    subtracao = eval(input("Digite na forma a - b - ... - n os valores que você quer subtrair\n"))
    print(float(subtracao))

def multiplicacao(): #Função multiplicação
    multiplicacao = eval(input("Digite na forma a * b * ... * n  os valores que você quer subtrair\n"))
    print(float(multiplicacao))

def divisao(): #Função divisão
    divisao = eval(input("Digite na forma a/b os valores que você quer dividir\n"))
    print(float(divisao))

def expressoes():
    expressao = eval(input("Digite aqui a expressão que você deseja calcular.\n"))
    print(float(expressao))

def retornar_menu():
    mais_op = int(input("Você deseja realizar mais alguma operação ?\n Sim (1)\n Não (0)\n"))
    if mais_op == 1:
        menu()
    else:
        exit()

def menu_basico():
    menu_bas = int(input("Selecione qual operação você quer utilizar\n 1. Soma\n 2. Subtração\n 3. Multiplicação\n 4. Divisao\n 5. Expresões\n"))
    if menu_bas == 1:
        soma()
        retornar_menu()
    else:
        pass

    if menu_bas == 2:
        subtracao()
        retornar_menu()
    else:
        pass
    
    if menu_bas == 3:
        multiplicacao()
        retornar_menu()
    else:
        pass
    
    if menu_bas == 4:
        divisao()
        retornar_menu()
    else:
        pass

    if menu_bas == 5:
        expressoes()
        retornar_menu()
    else:
        pass

def menu(): #Função menu
    opcao = int(input("Selecione qual funcção da calculadora você quer utilizar:\n 0. Sair\n 1. Básica\n"))
    if opcao == 1:
        print("Você selecionou a calculadora básica.")
        menu_basico()  

menu()
