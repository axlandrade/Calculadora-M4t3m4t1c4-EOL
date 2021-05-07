#Funções da Calculadora básica

import ast

def funcao_basica(): #Menu da calculadora básica
    print("Aqui nessa função você pode realizar operações como:\n 1. Soma (a+b)\n 2. Subtração (a-b)\n 3. Multiplicação (a*b)\n 4. Divisão (a/b)\n")
    funcao_bas = eval(input("Digite aqui a sua operação matemática.\n"))
    print(float(funcao_bas))
    retornar_menu()

import time

def retornar_menu(): #Função para retornar ao menu(menu())
    mais_op = int(input("Você deseja realizar mais alguma operação ?\n Sim (1)\n Não (0)\n"))
    if mais_op == 1:
        menu()
    else:
        print("Obrigado por usar a M4t3m4t1c4.")
        time.sleep(3)
        exit()

#Funções da Calculadora de Equações

from sympy import symbols, Eq, solve

def eq_1_grau(): #Função para resolver equações do 1º grau
    x = symbols('x')
    expr = input("Digite a sua equação na forma 'a * x + b'\n")
    sol = solve(expr)
    print(sol)
    retornar_menu()

def menu_eq(): #Menu da calculadora de equações
    opcao_eq = int(input("Selecione qual tipo de equação você deseja resolver\n 0. Voltar ao menu\n 1. Equação de 1º grau\n"))
    if opcao_eq == 0:
        menu()
    
    if opcao_eq == 1:
        eq_1_grau()


#Menu principal do programa

def menu(): #Função menu
    opcao = int(input("Selecione qual função da calculadora você quer utilizar:\n 0. Sair\n 1. Básica\n 2. Calculadora de equações\n"))
    if opcao ==0:
        print("Obrigado por usar a M4t3m4t1c4.")
        time.sleep(3)
        exit()
    
    if opcao == 1:
        print("Você selecionou a calculadora básica.")
        funcao_basica()
    else:
        pass

    if opcao == 2:
        print("Você selecionou a calculadora de equações")
        menu_eq()


menu()
