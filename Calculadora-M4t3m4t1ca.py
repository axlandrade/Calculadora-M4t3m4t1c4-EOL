#Funções da Calculadora básica

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

def expressoes(): #Função expressão
    expressao = eval(input("Digite aqui a expressão que você deseja calcular.\n"))
    print(float(expressao))

def menu_basico(): #Menu da calculadora básica
    menu_bas = int(input("Selecione qual operação você quer utilizar\n 0. Voltar ao menu\n 1. Soma\n 2. Subtração\n 3. Multiplicação\n 4. Divisao\n 5. Expressões\n"))
    if menu_bas == 0:
        menu()
    
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

def retornar_menu(): #Função para retornar ao menu(menu())
    mais_op = int(input("Você deseja realizar mais alguma operação ?\n Sim (1)\n Não (0)\n"))
    if mais_op == 1:
        menu()
    else:
        exit()

#Funções da Calculadora de Equações

from sympy import symbols, Eq, solve

def eq_1_grau():
    x = symbols('x')
    expr = input("Digite a sua equação na forma 'a * x + b'\n")
    sol = solve(expr)
    print(sol)
    retornar_menu()

def menu_eq():
    opcao_eq = int(input("Selecione qual tipo de equação você deseja resolver\n 0. Voltar ao menu\n 1. Equação de 1º grau\n"))
    if opcao_eq == 0:
        menu()
    
    if opcao_eq == 1:
        eq_1_grau()


#Menu principal do programa

def menu(): #Função menu
    opcao = int(input("Selecione qual função da calculadora você quer utilizar:\n 0. Sair\n 1. Básica\n 2. Calculadora de equações\n"))
    if opcao == 1:
        print("Você selecionou a calculadora básica.")
        menu_basico()
    else:
        pass

    if opcao == 2:
        print("Você selecionou a calculadora de equações")
        menu_eq()


menu()
